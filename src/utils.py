import json


def save_to_json(file, data: dict) -> None:
    with open(file=file, mode="rw") as f:
        json.dump(data, f)
