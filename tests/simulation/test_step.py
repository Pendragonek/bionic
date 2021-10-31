"""Test simulation step"""

from typing import List

import pytest

from bionic.buildings.steam_turbine import SteamTurbine
from bionic.elements.element import Element
from bionic.resources.resource_bank import ResourceBank
from bionic.elements.steam import Steam
from bionic.elements.water import Water
from bionic.simulation.step import simulation_step
from tests.buildings.test_geyser import TEST_GEYSER, TEST_GEYSER_OUTPUT_ELEMENT


@pytest.mark.parametrize(
    "current_time, initial_state, expected_state",
    [
        (0, [], [TEST_GEYSER_OUTPUT_ELEMENT]),
        (0, [Steam(2000, 125)], [Water(2000, 95), TEST_GEYSER_OUTPUT_ELEMENT]),
    ],
)
def test_simulation_step(
    current_time: int, initial_state: List[Element], expected_state: List[Element]
):
    """Test simulation step"""
    steam_turbine = SteamTurbine()
    element_bank = ResourceBank(*initial_state)
    simulation_step(steam_turbine, TEST_GEYSER, element_bank, current_time)
    assert element_bank.resource_dict == ResourceBank(*expected_state).resource_dict
