"""Test entity"""
from typing import List

import pytest

from bionic.buildings.geyser import Geyser
from bionic.elements import STEAM
from bionic.entities import Entity, EntityBank

TEST_OUTPUT_ENTITY = Entity(STEAM, 1000, 110)
TEST_GEYSER = Geyser(TEST_OUTPUT_ENTITY, 10, 20, 2.4, 4.6)


@pytest.mark.parametrize(
    "current_time, expected",
    [
        (0, True),
        (10, False),
        (1500, False),
    ]
)
def test_geyser_is_erupting(current_time: int, expected: bool):
    """Test geyser is erupting"""
    assert TEST_GEYSER.is_erupting(current_time) is expected


@pytest.mark.parametrize(
    "current_time, expected",
    [
        (100, True),
        (1500, False),
    ]
)
def test_geyser_is_active(current_time: int, expected: bool):
    """Test geyser is active"""
    assert TEST_GEYSER.is_active(current_time) is expected


@pytest.mark.parametrize(
    "current_time, initial_state, expected_state",
    [
        (0, [], [TEST_OUTPUT_ENTITY]),
        (10, [], []),
    ]
)
def test_geyser_process(current_time: int, initial_state: List[Entity], expected_state: List[Entity]):
    """Test geyser is erupting"""
    entity_bank = EntityBank(*initial_state)
    TEST_GEYSER.process(entity_bank, current_time)
    assert entity_bank.entity_dict == EntityBank(*expected_state).entity_dict
