from fastapi import FastAPI, UploadFile, File
import numpy as np
import cv2

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Exam Scanner API running"}


@app.post("/api/scan")
async def scan_exam(file: UploadFile = File(...)):

    contents = await file.read()

    nparr = np.frombuffer(contents, np.uint8)

    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if image is None:
        return {"error": "Invalid image"}

    return {
        "status": "success"
    }
