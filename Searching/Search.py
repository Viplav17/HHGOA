from Face_Identification.Face_Extractor import Detect_Encode_Face
from Searching.Web_Search import find_faces_on_web


def Search(image_path: str):
    """
    Full pipeline entry point.

    1. Detects and encodes the face from image_path using Face_Identification.
    2. Searches the web for matching faces using the embedding + Google Lens.

    Args:
        image_path: Absolute or relative path to the input image file.

    Returns:
        (ref_vector, matches)
          ref_vector — 512-d ArcFace embedding of the input face.
          matches    — list of dicts with: id, title, page_url, image_url,
                       image, vector, cosine_distance.
    """
    # Step 1 — Face detection & encoding (Face_Identification)
    ref_vector = Detect_Encode_Face(image_path)

    # Step 2 — Web search & candidate filtering (Searching)
    matches = find_faces_on_web(ref_vector, image_path)

    return ref_vector, matches
