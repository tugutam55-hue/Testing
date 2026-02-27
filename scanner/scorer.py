def score_answers(detected, answer_key):

    correct = 0
    wrong = 0

    for q, ans in answer_key.items():

        if detected.get(q) == ans:
            correct += 1
        else:
            wrong += 1

    total = len(answer_key)

    score = (correct / total) * 100 if total > 0 else 0

    return {
        "correct": correct,
        "wrong": wrong,
        "score": score
    }
