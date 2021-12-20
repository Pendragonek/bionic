"""Test element bank"""

from typing import Dict, List, Type

import pytest

from bionic.elements.element import Element
from bionic.resources.resource_bank import ResourceBank
from bionic.elements.water import Water


@pytest.mark.parametrize(
    "first_argument_list, second_argument_list",
    [
        ([Water(1000, 50)], [Water(1000, 50)]),
        ([Water(1000, 50), Water(2000, 50)], [Water(3000, 50)]),
    ],
)
def test_resource_bank_init(
    first_argument_list: List[Element], second_argument_list: List[Element]
):
    """Test resource bank init"""
    assert ResourceBank(*first_argument_list) == ResourceBank(*second_argument_list)


@pytest.mark.parametrize(
    "initial_state, requested_element_type, expected_element",
    [
        ([Water(1000, 50)], Water, Water(1000, 50)),
        ([], Water, Water(0, 0)),
    ],
)
def test_resource_bank_get(
    initial_state: List[Element],
    requested_element_type: Type[Element],
    expected_element: Element,
):
    """Test resource bank get"""
    element_bank = ResourceBank(*initial_state)
    assert element_bank.get(requested_element_type) == expected_element


@pytest.mark.parametrize(
    "initial_state, added_element, expected_state",
    [
        ([Water(1000)], Water(2000), [Water(3000)]),
        ([Water(1000)], Water(-2000), [Water(-1000)]),
        ([Water(1000)], Water(-1000), []),
        ([], Water(1000), [Water(1000)]),
        ([], Water(0), []),
    ],
)
def test_resource_bank_add(
    initial_state: List[Element], added_element: Element, expected_state: List[Element]
):
    """Test element bank add"""
    element_bank = ResourceBank(*initial_state)
    element_bank.add(added_element)
    assert element_bank.resource_dict == ResourceBank(*expected_state).resource_dict


@pytest.mark.parametrize(
    "initial_state, removed_element, expected_state",
    [
        ([Water(2000)], Water(1000), [Water(1000)]),
        ([Water(2000)], Water(2000), []),
        ([], Water(0), []),
        ([Water(1000)], Water(2000), [Water(-1000)]),
        ([], Water(1000), [Water(-1000)]),
    ],
)
def test_resource_bank_remove(
    initial_state: List[Element],
    removed_element: Element,
    expected_state: List[Element],
):
    """Test element bank remove"""
    element_bank = ResourceBank(*initial_state)
    element_bank.subtract(removed_element)
    assert element_bank.resource_dict == ResourceBank(*expected_state).resource_dict
