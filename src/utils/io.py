"""
Handles all file input output methods
"""
import json
from typing import Union, Dict, Any


def read_json(path: str) -> Union[list, Dict[Any, Any]]:
    with open(path, "r") as fp:
        content = json.load(fp)
    return content


def save_json(path: str, content: Any) -> None:
    with open(path, "w") as fp:
        json.dump(content, fp)
    return
