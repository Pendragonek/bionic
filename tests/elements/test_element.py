"""Test element"""

import pytest

from bionic.elements import Element, Hydrogen, Water


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
