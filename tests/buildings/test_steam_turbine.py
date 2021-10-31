"""Test steam turbine"""

from typing import List

import pytest

from bionic.buildings.steam_turbine import SteamTurbine
from bionic.elements.element import Element
from bionic.resources.resource_bank import ResourceBank
from bionic.elements.steam import Steam
from bionic.elements.water import Water


@pytest.mark.parametrize(
    "initial_state, expected_state",
    [
        (
            [Steam(4000, 150), Water(1000, 95)],
            [Steam(2000, 150), Water(3000, 95)],
        ),
        (
            [Steam(4000, 110)],
            [Steam(4000, 110)],
        ),
        (
            [Steam(1000, 150)],
            [Water(1000, 95)],
        ),
    ],
)
def test_steam_turbine_process(
    initial_state: List[Element], expected_state: List[Element]
):
    """Test Steam Turbine process"""
    steam_turbine = SteamTurbine()
    element_bank = ResourceBank(*initial_state)
    steam_turbine.process(element_bank)
    assert element_bank.resource_dict == ResourceBank(*expected_state).resource_dict
