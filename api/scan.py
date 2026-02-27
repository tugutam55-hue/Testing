from fastapi import FastAPI, UploadFile, File
import numpy as np
import cv2
import json

from scanner.preprocess import preprocess
from scanner.detector import detect_answers
from scanner.scorer import score_answers
from scanner.template_loader import load_template

app = FastAPI()


@app.post("/api/scan")
async def scan_exam(
    file: UploadFile = File(...),
    answer_key: str = None
):

    contents = await file.read()

    nparr = np.frombuffer(contents, np.uint8)

    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    thresh = preprocess(image)

    template = load_template()

    detected = detect_answers(template, thresh)

    if answer_key:
        key = json.loads(answer_key)
        score = score_answers(detected, key)
    else:
        score = {}

    return {
        "answers": detected,
        "result": score
  }
