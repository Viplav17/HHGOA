import io
import requests
import numpy as np
from PIL import Image
import serpapi
from Searching.Cosine import SERPAPI_API_KEY, MATCH_THRESHOLD, cosine_distance
from Searching.Image_Byte import _get_image_bytes
from Face_Identification.Face_Extractor import Detect_Encode_Face


def search_google_lens(image_bytes, api_key):
    """Uploads the image buffer to SerpApi and queries Google Lens."""
    upload_res = requests.post(
        "https://serpapi.com/image",
        files={"image": ("input.jpg", image_bytes, "image/jpeg")},
        data={"api_key": api_key},
        timeout=30
    ).json()

    image_id = upload_res.get("image_id")
    if not image_id:
        raise ValueError(f"SerpApi image upload failed: {upload_res}")

    client = serpapi.Client(api_key=api_key)
    search_params = {
        "engine": "google_lens",
        "image_id": image_id,
        "type": "visual_matches",
        "hl": "en"
    }
    results = client.search(search_params)
    return results.get("visual_matches", [])


def find_faces_on_web(ref_vector, incoming_image, api_key=SERPAPI_API_KEY, threshold=MATCH_THRESHOLD):
    """
    Searches the web for faces matching ref_vector.

    Args:
        ref_vector:     512-d ArcFace embedding from Face_Identification.Face_Extractor.
        incoming_image: The original image (PIL.Image, numpy array, bytes, or file path)
                        used to query Google Lens visually.
        api_key:        SerpApi key (defaults to token from API_tk).
        threshold:      Cosine distance cutoff — lower means stricter match.

    Returns:
        list of dicts with keys: id, title, page_url, image_url, image, vector, cosine_distance
    """
    img_bytes = _get_image_bytes(incoming_image)
    visual_matches = search_google_lens(img_bytes, api_key)

    results_list = []
    headers = {"User-Agent": "Mozilla/5.0"}

    for idx, match in enumerate(visual_matches):
        img_url = match.get("thumbnail")
        if not img_url:
            continue

        try:
            resp = requests.get(img_url, headers=headers, timeout=10)
            if resp.status_code != 200:
                continue

            # Save candidate thumbnail to a temp buffer so Detect_Encode_Face can read it
            candidate_img = Image.open(io.BytesIO(resp.content)).convert("RGB")
            candidate_arr = np.array(candidate_img)

            # Re-use Face_Identification's encoder for consistency
            try:
                from deepface import DeepFace
                embedding_objs = DeepFace.represent(
                    img_path=candidate_arr,
                    model_name="ArcFace",
                    detector_backend="mtcnn",
                    enforce_detection=True,
                    align=True
                )
                candidate_vector = embedding_objs[0]["embedding"]
            except Exception:
                continue

            distance = cosine_distance(ref_vector, candidate_vector)

            if distance <= threshold:
                results_list.append({
                    "id": idx,
                    "title": match.get("title"),
                    "page_url": match.get("link"),
                    "image_url": img_url,
                    "image": candidate_img,
                    "vector": candidate_vector,
                    "cosine_distance": float(distance)
                })
        except Exception:
            continue

    return results_list