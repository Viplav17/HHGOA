from Face_Identification.Face_Extractor import Detect_Encode_Face
from Searching.Web_Search import find_faces_on_web

def Search(image_path: str):
    """
    1. Encodes target face.
    2. Searches the web and returns candidate matches sorted by confidence.
    """
    ref_vector = Detect_Encode_Face(image_path)
    matches = find_faces_on_web(ref_vector, image_path)
    return matches