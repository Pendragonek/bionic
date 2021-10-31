"""Test element"""

from typing import List, Union

import pytest

from bionic.elements.element import Element, calculate_combined_element_temperature
from bionic.elements.hydrogen import Hydrogen
from bionic.elements.igneous_rock import IgneousRock
from bionic.elements.water import Water


@pytest.mark.parametrize(
    "element, expected_heat",
    [
        (Water(1000, 10), 41790),
        (Hydrogen(2000, 20), 96000),
    ],
)
def test_element_heat(element: Element, expected_heat: float):
    """Test element calculations"""
    assert element.heat == expected_heat


@pytest.mark.parametrize(
    "base_element, added_element, expected_element",
    [
        (Water(1000, 10), Water(1000, 10), Water(2000, 10)),
        (Water(1000, 10), Water(1000, 30), Water(2000, 20)),
        (Water(2000, 10), Water(1000, 40), Water(3000, 20)),
    ],
)
def test_element_add(
    base_element: Element, added_element: Element, expected_element: Element
):
    """Test element add"""
    assert base_element + added_element == expected_element


@pytest.mark.parametrize(
    "base_element, added_element",
    [
        (Water(1000, 10), Hydrogen(1000, 10)),
    ],
)
def test_element_add_exception(base_element: Element, added_element: Element):
    """Test element add exception"""
    with pytest.raises(TypeError):
        assert base_element + added_element


@pytest.mark.parametrize(
    "base_element, added_element, expected_element",
    [
        (Water(1000), 2, Water(2000)),
        (Water(1000), 0.5, Water(500)),
    ],
)
def test_element_multiply(
    base_element: Element, added_element: Union[int, float], expected_element: Element
):
    """Test element multiply"""
    assert base_element * added_element == expected_element


@pytest.mark.parametrize(
    "base_element, added_element, expected_element",
    [
        (Water(1000), 2, Water(500)),
        (Water(1000), 0.5, Water(2000)),
    ],
)
def test_element_divide(
    base_element: Element, added_element: Union[int, float], expected_element: Element
):
    """Test element divide"""
    assert base_element / added_element == expected_element


@pytest.mark.parametrize(
    "element_list, expected",
    [
        ([Hydrogen(1000, 10)], 10),
        ([Hydrogen(1000, 10), Hydrogen(1000, 40)], 25),
        ([Hydrogen(1000, 10), Hydrogen(4000, 40)], 34),
        ([Hydrogen(5000, 10), IgneousRock(4000, 40)], 17.5),
    ],
)
def test_calculate_combined_element_temperature(
    element_list: List[Element], expected: float
):
    """Test calculate combined element temperature"""
    combined_temperature = calculate_combined_element_temperature(*element_list)
    assert combined_temperature == expected
