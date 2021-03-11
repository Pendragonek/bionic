"""Test element"""

import pytest

from bionic.elements import Element


@pytest.mark.parametrize(
    "element_name, expected_key",
    [
        ("Water", "water"),
        ("Natural Gas", "natural_gas"),
    ]
)
def test_entity_key(element_name: str, expected_key: str):
    """Test entity key"""
    element = Element(element_name, 1.000)
    assert element.key == expected_key
