"""Test entity bank"""
from typing import List, Dict

import pytest

from bionic.dataclasses.entity import Entity
from bionic.dataclasses.entity_bank import EntityBank
from bionic.elements import Element, WATER


@pytest.mark.parametrize(
    "arguments_passed, expected_state",
    [
        ([Entity(WATER, 1000, 50)], {WATER.key: Entity(WATER, 1000, 50)}),
        ([Entity(WATER, 1000, 50), Entity(WATER, 2000, 50)], {WATER.key: Entity(WATER, 3000, 50)}),
    ]
)
def test_entity_bank_init(arguments_passed: List[Entity], expected_state: Dict[str, Entity]):
    """Test entity bank init"""
    assert EntityBank(*arguments_passed).entity_dict == expected_state


@pytest.mark.parametrize(
    "initial_state, requested_element, expected_entity",
    [
        ([Entity(WATER, 1000, 50)], WATER, Entity(WATER, 1000, 50)),
        ([], WATER, Entity(WATER, 0, 0)),
    ]
)
def test_entity_bank_get(initial_state: List[Entity], requested_element: Element, expected_entity: float):
    """Test entity bank get"""
    entity_bank = EntityBank(*initial_state)
    assert entity_bank.get(requested_element) == expected_entity


@pytest.mark.parametrize(
    "initial_state, added_entity, expected_state",
    [
        ([Entity(WATER, 1000, 50)], Entity(WATER, 2000, 50), [Entity(WATER, 3000, 50)]),
        ([], Entity(WATER, 1000, 50), [Entity(WATER, 1000, 50)]),
    ]
)
def test_entity_bank_add(initial_state: List[Entity], added_entity: Entity, expected_state: List[Entity]):
    """Test entity bank add"""
    entity_bank = EntityBank(*initial_state)
    entity_bank.add(added_entity)
    assert entity_bank.entity_dict == EntityBank(*expected_state).entity_dict


@pytest.mark.parametrize(
    "initial_state, removed_entity, expected_state",
    [
        ([Entity(WATER, 2000, 50)], Entity(WATER, 1000, 50), [Entity(WATER, 1000, 50)]),
        ([], Entity(WATER, 0, 50), []),
    ]
)
def test_entity_bank_remove(initial_state: List[Entity], removed_entity: Entity, expected_state: List[Entity]):
    """Test entity bank remove"""
    entity_bank = EntityBank(*initial_state)
    entity_bank.remove(removed_entity)
    assert entity_bank.entity_dict == EntityBank(*expected_state).entity_dict


@pytest.mark.parametrize(
    "initial_state, removed_entity",
    [
        ([Entity(WATER, 1000, 50)], Entity(WATER, 2000, 50)),
        ([], Entity(WATER, 1000, 50)),
    ]
)
def test_entity_bank_remove_exception(initial_state: List[Entity], removed_entity: Entity):
    """Test entity bank remove"""
    entity_bank = EntityBank(*initial_state)
    with pytest.raises(ArithmeticError):
        entity_bank.remove(removed_entity)
