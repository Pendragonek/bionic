"""Test element"""
from typing import List

import pytest

from bionic.elements import Element, Hydrogen, IgneousRock, Water
from bionic.elements.element import calculate_combined_element_temperature


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


@pytest.mark.parametrize(
    "element_list, expected",
    [
        ([Hydrogen(1000, 10)], 10),
        ([Hydrogen(1000, 10), Hydrogen(1000, 40)], 25),
        ([Hydrogen(1000, 10), Hydrogen(4000, 40)], 34),
        ([Hydrogen(5000, 10), IgneousRock(4000, 40)], 17.5),
    ]
)
def test_calculate_combined_element_temperature(element_list: List[Element], expected: float):
    """Test calculate combined element temperature"""
    combined_temperature = calculate_combined_element_temperature(*element_list)
    assert combined_temperature == expected
