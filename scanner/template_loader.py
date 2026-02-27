import json

def load_template(path="templates/default.json"):
    with open(path) as f:
        return json.load(f)
