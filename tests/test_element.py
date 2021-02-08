"""Test element"""
from pathlib import Path

from bionic.dataclasses import load_element_dict_from_file


def test_load_element_dict_from_file():
    """Test loading dictionary of element from a file"""
    test_file_path = Path("tests/resources/test_element.json")

    element_dict = load_element_dict_from_file(test_file_path)

    assert element_dict.keys() == {"element_key"}
    assert element_dict["element_key"].name == "element_name"
    assert element_dict["element_key"].shc == 1
