import cv2

def compute_density(thresh, box):

    x,y,w,h = box

    roi = thresh[y:y+h, x:x+w]

    total = w*h

    filled = cv2.countNonZero(roi)

    density = filled / total

    return density


def detect_answers(template, thresh):

    results = {}

    for q in template["questions"]:

        qnum = q["number"]

        densities = {}

        for opt, box in q["options"].items():
            densities[opt] = compute_density(thresh, box)

        best = max(densities, key=densities.get)

        if densities[best] < 0.15:
            results[qnum] = None
        else:
            results[qnum] = best

    return results
