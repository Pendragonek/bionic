"""Test entity bank"""
from typing import List

import pytest

from bionic.dataclasses.entity import Entity
from bionic.dataclasses.entity_bank import EntityBank
from bionic.elements import Element, WATER


@pytest.mark.parametrize(
    "entity_list, element, expected_entity",
    [
        ([Entity(WATER, 1000, 50)], WATER, Entity(WATER, 1000, 50))
    ]
)
def test_entity_bank_get_item(entity_list: List[Entity], element: Element, expected_entity: float):
    """Test entity bank get amount"""
    entity_bank = EntityBank(entity_list)
    assert entity_bank[element] == expected_entity
