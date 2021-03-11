"""Test Steam Turbine"""
from typing import Dict

import pytest

from bionic.buildings.steam_turbine import SteamTurbine
from bionic.dataclasses import Entity, STEAM, WATER


@pytest.mark.parametrize(
    "initial_state, expected_state",
    [
        (
            {"steam": Entity(STEAM, 4000, 150), "water": Entity(STEAM, 1000, 95)},
            {"steam": Entity(STEAM, 2000, 150), "water": Entity(STEAM, 3000, 95)},
        ),
        (
            {"steam": Entity(STEAM, 4000, 110)},
            {"steam": Entity(STEAM, 4000, 110)},
        ),
        (
            {"steam": Entity(STEAM, 1000, 150)},
            {"water": Entity(WATER, 1000, 95)},
        ),
    ]
)
def test_steam_turbine_process(initial_state: Dict[str, Entity], expected_state: Dict[str, Entity]):
    steam_turbine = SteamTurbine()
    steam_turbine.process(initial_state)
    assert initial_state == expected_state
