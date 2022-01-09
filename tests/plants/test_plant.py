"""Test plant"""
from typing import List

import pytest

from bionic.elements.dirt import Dirt
from bionic.elements.ethanol import Ethanol
from bionic.elements.water import Water
from bionic.food.bristle_berry import BristleBerry
from bionic.food.nosh_bean import NoshBean
from bionic.plants.bristle_blossom import BristleBlossom
from bionic.plants.nosh_sprout import NoshSprout
from bionic.plants.plant import Plant
from bionic.resources.resource import Resource


@pytest.mark.parametrize(
    "plant, expected_production, expected_consumption",
    [
        (NoshSprout(), [NoshBean(amount=1 / 7)], []),
        (
            NoshSprout(domesticated=True),
            [NoshBean(amount=4 / 7)],
            [Ethanol(amount=20000), Dirt(amount=5000)],
        ),
        (
            BristleBlossom(domesticated=True),
            [BristleBerry(amount=1 / 6)],
            [Water(amount=20000)],
        ),
    ],
)
def test_plant(
    plant: Plant,
    expected_production: List[Resource],
    expected_consumption: List[Resource],
):
    """Test plant"""
    assert plant.resource_production_per_unit == expected_production
    assert plant.resource_consumption_per_unit == expected_consumption
