import cv2
import json
from deepface import DeepFace

MODEL_NAME = "ArcFace" 
DETECTOR = "mtcnn" 

def extract_and_prepare(image_path: str):
    """
    Detects a face, extracts the embedding, and returns the data. Takes image location as input.
    """
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Cannot open '{image_path}'") #error line if image does not open

    results = DeepFace.represent(
        img_path=img,
        model_name=MODEL_NAME,
        detector_backend=DETECTOR,
        enforce_detection=True,
        align=True
    )

    face = results[0] 
    area = face["facial_area"]
    embedding = face["embedding"] 
    """""""""""

    Up until here was only for getting the vector needed that is unique to each face

    Next, the cropped image that only includes the face and no other background

    """""""""""

    x, y, w, h = area["x"], area["y"], area["w"], area["h"]
    face_crop = img[y:y + h, x:x + w]
    
    
    cv2.imwrite("face_crop.jpg", face_crop)

    payload = {
        "model": MODEL_NAME,
        "detector_backend": DETECTOR,
        "embedding": embedding,
        "vector_dim": len(embedding)
    }        



    with open("face_data.json", "w") as f:
        json.dump(payload, f, indent=2)

    # Returns the actual variables
    return face_crop, payload

if __name__ == "__main__":
    crop, data = extract_and_prepare("Face Identification/img1.png")
    print(f"Test successful. Extracted {data['vector_dim']}-dim vector.")
    print(data, crop)