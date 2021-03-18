"""Test simulation step"""
from typing import List

import pytest

from bionic.buildings.steam_turbine import SteamTurbine
from bionic.elements import STEAM, WATER
from bionic.entities import Entity, EntityBank
from bionic.simulation.step import simulation_step
from tests.buildings.test_geyser import TEST_GEYSER, TEST_GEYSER_OUTPUT_ENTITY


@pytest.mark.parametrize(
    "current_time, initial_state, expected_state",
    [
        (0, [], [TEST_GEYSER_OUTPUT_ENTITY]),
        (0, [Entity(STEAM, 2000, 125)], [Entity(WATER, 2000, 95), TEST_GEYSER_OUTPUT_ENTITY]),
    ]
)
def test_simulation_step(current_time: int, initial_state: List[Entity], expected_state: List[Entity]):
    steam_turbine = SteamTurbine()
    entity_bank = EntityBank(*initial_state)
    simulation_step(steam_turbine, TEST_GEYSER, entity_bank, current_time)
    assert entity_bank.entity_dict == EntityBank(*expected_state).entity_dict
