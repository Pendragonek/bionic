"""Test Steam Turbine"""
from typing import List

import pytest

from bionic.buildings.steam_turbine import SteamTurbine
from bionic.entities import Entity
from bionic.entities.entity_bank import EntityBank
from bionic.elements import STEAM, WATER


@pytest.mark.parametrize(
    "initial_state, expected_state",
    [
        (
            [Entity(STEAM, 4000, 150), Entity(WATER, 1000, 95)],
            [Entity(STEAM, 2000, 150), Entity(WATER, 3000, 95)],
        ),
        (
            [Entity(STEAM, 4000, 110)],
            [Entity(STEAM, 4000, 110)],
        ),
        (
            [Entity(STEAM, 1000, 150)],
            [Entity(STEAM, 0, 150), Entity(WATER, 1000, 95)],
        ),
    ]
)
def test_steam_turbine_process(initial_state: List[Entity], expected_state: List[Entity]):
    steam_turbine = SteamTurbine()
    entity_bank = EntityBank(*initial_state)
    steam_turbine.process(entity_bank)
    assert entity_bank.entity_dict == EntityBank(*expected_state).entity_dict
