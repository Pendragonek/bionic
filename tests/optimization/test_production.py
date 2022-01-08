"""Test production"""

import pytest

from bionic.buildings.geyser import Geyser
from bionic.elements.hydrogen import Hydrogen
from bionic.optimization.production import calculate_geyser_average_production


@pytest.mark.parametrize(
    "geyser, expected_production",
    [
        (
            Geyser(
                output_element=Hydrogen(amount=1000),
                eruption_time=1,
                eruption_period=2,
                activity_time=1,
                activity_period=2,
            ),
            Hydrogen(amount=250),
        )
    ],
)
def test_calculate_geyser_average_production(geyser, expected_production):
    """Test calculate geyser average production function"""
    calculated_production = calculate_geyser_average_production(geyser)
    assert calculated_production == expected_production
