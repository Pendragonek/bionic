"""Dataclasses"""
import json
from pathlib import Path
from typing import Dict

from bionic.dataclasses.element import Element


def load_element_dict_from_file(file_path: Path) -> Dict[str, Element]:
    """Loads element dictionary from specified json file"""
    with file_path.open() as file:
        file_content_dict: Dict[str, Dict] = json.load(file)

    element_dict: Dict[str, Element] = dict()
    for key, value_dict in file_content_dict.items():
        element_dict[key] = Element(**value_dict)

    return element_dict
