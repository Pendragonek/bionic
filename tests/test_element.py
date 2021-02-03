"""Test element"""
import json
from pathlib import Path
from tempfile import NamedTemporaryFile

from bionic.dataclasses import load_element_dict_from_file


def test_load_element_dict_from_file():
    """Test loading dictionary of element from a file"""
    test_file_content = {
        "element_key": {
            "name": "element_name",
            "shc": 1,
        }
    }
    with NamedTemporaryFile() as test_file:
        test_file.write(json.dumps(test_file_content).encode())
        test_file.flush()
        test_file_path = Path(test_file.name)

        element_dict = load_element_dict_from_file(test_file_path)

    assert test_file_content.keys() == element_dict.keys()
    assert element_dict["element_key"].name == "element_name"
    assert element_dict["element_key"].shc == 1
