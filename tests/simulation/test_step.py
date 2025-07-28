"""Test simulation step."""

import pytest

from bionic.processors.buildings import SteamTurbine
from bionic.resources import ResourceBank
from bionic.resources.elements import Element, Steam, Water
from bionic.simulation.step import simulation_step
from tests.processors.buildings.test_geyser import (
    TEST_GEYSER,
    TEST_GEYSER_OUTPUT_ELEMENT,
)


@pytest.mark.parametrize(
    ("current_time", "initial_state", "expected_state"),
    [
        (0, [], [TEST_GEYSER_OUTPUT_ELEMENT]),
        (
            0,
            [Steam(amount=2000, temperature=125)],
            [Water(amount=2000, temperature=95), TEST_GEYSER_OUTPUT_ELEMENT],
        ),
    ],
)
def test_simulation_step(
    current_time: int,
    initial_state: list[Element],
    expected_state: list[Element],
) -> None:
    """Test simulation step."""
    steam_turbine = SteamTurbine()
    element_bank = ResourceBank(*initial_state)
    simulation_step(steam_turbine, TEST_GEYSER, element_bank, current_time)
    assert element_bank.resource_dict == ResourceBank(*expected_state).resource_dict
