"""Test production"""
import pytest

from bionic.buildings import Geyser
from bionic.elements import Hydrogen
from bionic.optimization.production import calculate_geyser_average_production


@pytest.mark.parametrize(
    "geyser, expected_production", [(Geyser(Hydrogen(1000), 1, 2, 1, 2), Hydrogen(250))]
)
def test_calculate_geyser_average_production(geyser, expected_production):
    """Test calculate geyser average production function"""
    calculated_production = calculate_geyser_average_production(geyser)
    assert calculated_production == expected_production
