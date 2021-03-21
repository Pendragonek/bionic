"""Test element"""

import pytest

from bionic.elements import Element, Hydrogen, Water


@pytest.mark.parametrize(
    "element, expected_heat",
    [
        (Water(1000, 10), 41790),
        (Hydrogen(2000, 20), 96000),
    ]
)
def test_element_heat(element: Element, expected_heat: float):
    """Test element calculations"""
    assert element.heat == expected_heat
