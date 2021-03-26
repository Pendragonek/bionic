"""Test element bank"""
from typing import Dict, List, Type

import pytest

from bionic.elements import Element, ElementBank, Hydrogen, IgneousRock, Water


@pytest.mark.parametrize(
    "arguments_passed, expected_state",
    [
        ([Water(1000, 50)], {Water: Water(1000, 50)}),
        ([Water(1000, 50), Water(2000, 50)], {Water: Water(3000, 50)}),
    ],
)
def test_element_bank_init(
    arguments_passed: List[Element], expected_state: Dict[Type[Element], Element]
):
    """Test element bank init"""
    assert ElementBank(*arguments_passed).element_dict == expected_state


@pytest.mark.parametrize(
    "initial_state, requested_element_type, expected_element",
    [
        ([Water(1000, 50)], Water, Water(1000, 50)),
        ([], Water, Water(0, 0)),
    ],
)
def test_element_bank_get(
    initial_state: List[Element],
    requested_element_type: Type[Element],
    expected_element: Element,
):
    """Test element bank get"""
    element_bank = ElementBank(*initial_state)
    assert element_bank.get(requested_element_type) == expected_element


@pytest.mark.parametrize(
    "initial_state, added_element, expected_state",
    [
        ([Water(1000, 50)], Water(2000, 80), [Water(3000, 70)]),
        ([], Water(1000, 50), [Water(1000, 50)]),
        ([], Water(0, 0), [Water(0, 0)]),
    ],
)
def test_element_bank_add(
    initial_state: List[Element], added_element: Element, expected_state: List[Element]
):
    """Test element bank add"""
    element_bank = ElementBank(*initial_state)
    element_bank.add(added_element)
    assert element_bank.element_dict == ElementBank(*expected_state).element_dict


@pytest.mark.parametrize(
    "initial_state, removed_element, expected_state",
    [
        ([Water(2000, 50)], Water(1000, 50), [Water(1000, 50)]),
        ([], Water(0, 50), []),
    ],
)
def test_element_bank_remove(
    initial_state: List[Element],
    removed_element: Element,
    expected_state: List[Element],
):
    """Test element bank remove"""
    element_bank = ElementBank(*initial_state)
    element_bank.remove(removed_element)
    assert element_bank.element_dict == ElementBank(*expected_state).element_dict


@pytest.mark.parametrize(
    "initial_state, removed_element",
    [
        ([Water(1000, 50)], Water(2000, 50)),
        ([], Water(1000, 50)),
    ],
)
def test_element_bank_remove_exception(
    initial_state: List[Element], removed_element: Element
):
    """Test element bank remove exception"""
    element_bank = ElementBank(*initial_state)
    with pytest.raises(ArithmeticError):
        element_bank.remove(removed_element)


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
    combined_temperature = ElementBank.calculate_combined_element_temperature(
        *element_list
    )
    assert combined_temperature == expected
