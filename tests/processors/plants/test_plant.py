"""Test plant."""

import pytest

from bionic.processors.plants import NoshSprout
from bionic.processors.plants.bristle_blossom import BristleBlossom
from bionic.processors.plants.plant import Plant
from bionic.resources import Resource
from bionic.resources.elements import Dirt, Ethanol, Water
from bionic.resources.food import BristleBerry, NoshBean


@pytest.mark.parametrize(
    ("plant", "expected_production", "expected_consumption"),
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
    expected_production: list[Resource],
    expected_consumption: list[Resource],
) -> None:
    """Test plant."""
    assert plant.resource_production_per_unit == expected_production
    assert plant.resource_consumption_per_unit == expected_consumption
