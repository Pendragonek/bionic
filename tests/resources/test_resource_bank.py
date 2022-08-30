"""Test element bank"""

from typing import List, Type

import pytest

from bionic.resources import ResourceBank
from bionic.resources.elements import Element, Water


@pytest.mark.parametrize(
    "first_argument_list, second_argument_list",
    [
        ([Water(amount=1000, temperature=50)], [Water(amount=1000, temperature=50)]),
        (
            [Water(amount=1000, temperature=50), Water(amount=2000, temperature=50)],
            [Water(amount=3000, temperature=50)],
        ),
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
        (
            [Water(amount=1000, temperature=50)],
            Water,
            Water(amount=1000, temperature=50),
        ),
        ([], Water, Water()),
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
        ([Water(amount=1000)], Water(amount=2000), [Water(amount=3000)]),
        ([Water(amount=1000)], Water(amount=-2000), [Water(amount=-1000)]),
        ([Water(amount=1000)], Water(amount=-1000), []),
        ([], Water(amount=1000), [Water(amount=1000)]),
        ([], Water(), []),
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
        ([Water(amount=2000)], Water(amount=1000), [Water(amount=1000)]),
        ([Water(amount=2000)], Water(amount=2000), []),
        ([], Water(), []),
        ([Water(amount=1000)], Water(amount=2000), [Water(amount=-1000)]),
        ([], Water(amount=1000), [Water(amount=-1000)]),
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
