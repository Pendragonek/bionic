"""Test element"""

from typing import List, Union

import pytest

from bionic.resources.elements import Element, Hydrogen, IgneousRock, Water
from bionic.resources.elements.element import calculate_combined_element_temperature


@pytest.mark.parametrize(
    "element, expected_heat",
    [
        (Water(amount=1000, temperature=10), 41790),
        (Hydrogen(amount=2000, temperature=20), 96000),
    ],
)
def test_element_heat(element: Element, expected_heat: float):
    """Test element calculations"""
    assert element.heat == expected_heat


@pytest.mark.parametrize(
    "base_element, added_element, expected_element",
    [
        (
            Water(amount=1000, temperature=10),
            Water(amount=1000, temperature=10),
            Water(amount=2000, temperature=10),
        ),
        (
            Water(amount=1000, temperature=10),
            Water(amount=1000, temperature=30),
            Water(amount=2000, temperature=20),
        ),
        (
            Water(amount=2000, temperature=10),
            Water(amount=1000, temperature=40),
            Water(amount=3000, temperature=20),
        ),
    ],
)
def test_element_temperature_add(
    base_element: Element, added_element: Element, expected_element: Element
):
    """Test element add"""
    assert base_element.temperature_add(added_element) == expected_element


@pytest.mark.parametrize(
    "base_element, added_element",
    [
        (Water(amount=1000, temperature=10), Hydrogen(amount=1000, temperature=10)),
    ],
)
def test_element_temperature_add_exception(
    base_element: Element, added_element: Element
):
    """Test element add exception"""
    with pytest.raises(TypeError):
        assert base_element.temperature_add(added_element)


@pytest.mark.parametrize(
    "base_element, added_element, expected_element",
    [
        (Water(amount=1000), 2, Water(amount=2000)),
        (Water(amount=1000), 0.5, Water(amount=500)),
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
        (Water(amount=1000), 2, Water(amount=500)),
        (Water(amount=1000), 0.5, Water(amount=2000)),
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
        ([Hydrogen(amount=1000, temperature=10)], 10),
        (
            [
                Hydrogen(amount=1000, temperature=10),
                Hydrogen(amount=1000, temperature=40),
            ],
            25,
        ),
        (
            [
                Hydrogen(amount=1000, temperature=10),
                Hydrogen(amount=4000, temperature=40),
            ],
            34,
        ),
        (
            [
                Hydrogen(amount=5000, temperature=10),
                IgneousRock(amount=4000, temperature=40),
            ],
            17.5,
        ),
    ],
)
def test_calculate_combined_element_temperature(
    element_list: List[Element], expected: float
):
    """Test calculate combined element temperature"""
    combined_temperature = calculate_combined_element_temperature(*element_list)
    assert combined_temperature == expected
