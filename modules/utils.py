import json
from typing import Any


def write_json(filename: str, obj: Any):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
