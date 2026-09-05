import cv2
from deepface import DeepFace

MODEL_NAME = "ArcFace" 
DETECTOR = "mtcnn" 

def Detect_Encode_Face(image_path: str):
    """
    Detects a face, extracts the embedding, and returns the data. Takes image location as input.
    """
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Cannot open '{image_path}'") 

    results = DeepFace.represent(
        img_path=img,
        model_name=MODEL_NAME,
        detector_backend=DETECTOR,
        enforce_detection=True,
        align=True
    )

    face = results[0] 
    embedding = face["embedding"] 

    # Returns the actual variables
    return embedding

