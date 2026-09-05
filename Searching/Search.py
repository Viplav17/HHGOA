import io
import requests
from PIL import Image
from APIt import deepface_tk
from encode import extract_face_vector
from cosine_distance import cosine_distance
from search_web import search_web_for_faces

FACECHECK_API_TOKEN = deepface_tk
INPUT_IMAGE_PATH = "my_face.jpg"
MATCH_THRESHOLD = 0.5


def run_pipeline(reference_image_path):
    # encode the input photo into a vector (encoding)
    print("1. Encoding original face into vector space...")
    ref_vector = extract_face_vector(reference_image_path)
    if not ref_vector:
        raise ValueError("No face detected in reference image!")
    print(f"   Encoded reference vector: {len(ref_vector)}-dimensions")

    # task 2
    print("2. Searching open web for face matches...")
    web_candidates = search_web_for_faces(reference_image_path)
    print(f"   Received {len(web_candidates)} candidates from web search.")

    # Step 3: get image from web
    results_list = []
    print("3. Vectorizing downloaded matches and verifying identity...")

    for idx, item in enumerate(web_candidates):
        img_url = item.get("base64") or item.get("url")
        if not img_url or not img_url.startswith("http"):
            continue

        try:
            # Download image bytes
            resp = requests.get(img_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
            if resp.status_code != 200:
                continue

            candidate_img = Image.open(io.BytesIO(resp.content)).convert("RGB")

            # Encode candidate face into a 512-d vector
            candidate_vector = extract_face_vector(candidate_img)
            if candidate_vector is None:
                continue

            # Verify mathematically against our reference vector
            distance = cosine_distance(ref_vector, candidate_vector)

            if distance <= MATCH_THRESHOLD:
                print(f"   [MATCH #{len(results_list)+1}] Distance: {distance:.4f} | Source: {img_url}")

                # Append structured output
                results_list.append({
                    "id": idx,
                    "source_url": img_url,
                    "image": candidate_img,
                    "vector": candidate_vector,
                    "cosine_distance": float(distance)
                })
        except Exception:
            continue

    return ref_vector, results_list


if __name__ == "__main__":
    original_vector, matched_results = run_pipeline(INPUT_IMAGE_PATH)

    print(f"\nTotal verified items returned: {len(matched_results)}")

    if matched_results:
        first_match = matched_results[0]
        match_image = first_match["image"]
        match_vector = first_match["vector"]
        print(f"First match vector length: {len(match_vector)}")