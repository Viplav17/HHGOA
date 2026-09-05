import io
import time
import requests
from PIL import Image
from APIt import deepface_tk

FACECHECK_API_TOKEN = deepface_tk

def search_web_for_faces(image_path):
    
    headers = {"Authorization": f"Bearer {FACECHECK_API_TOKEN}"}
    
    with open(image_path, "rb") as f:
        res = requests.post("https://facecheck.id/api/upload_pic", headers=headers, files={"images": f})
    
    data = res.json()
    search_id = data.get("id_search")
    if not search_id:
        raise RuntimeError(f"Search initialization failed: {data}")

    while True:
        payload = {"id_search": search_id, "with_progress": True}
        check = requests.post("https://facecheck.id/api/search", headers=headers, json=payload).json()
        
        if check.get("output"):
            return check["output"]["items"]
        if check.get("error"):
            raise RuntimeError(check["error"])
            
        time.sleep(2.5)

