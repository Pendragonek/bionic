"""Test steam turbine"""

from typing import List

import pytest

from bionic.buildings.steam_turbine import SteamTurbine
from bionic.elements.element import Element
from bionic.elements.element_bank import ElementBank
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
            [Steam(0, 150), Water(1000, 95)],
        ),
    ],
)
def test_steam_turbine_process(
    initial_state: List[Element], expected_state: List[Element]
):
    """Test Steam Turbine process"""
    steam_turbine = SteamTurbine()
    element_bank = ElementBank(*initial_state)
    steam_turbine.process(element_bank)
    assert element_bank.element_dict == ElementBank(*expected_state).element_dict
