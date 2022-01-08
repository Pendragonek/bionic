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
            [Steam(amount=4000, temperature=150), Water(amount=1000, temperature=95)],
            [Steam(amount=2000, temperature=150), Water(amount=3000, temperature=95)],
        ),
        (
            [Steam(amount=4000, temperature=110)],
            [Steam(amount=4000, temperature=110)],
        ),
        (
            [Steam(amount=1000, temperature=150)],
            [Water(amount=1000, temperature=95)],
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
