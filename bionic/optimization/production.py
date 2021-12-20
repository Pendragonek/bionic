"""Production"""

from bionic.buildings.geyser import Geyser
from bionic.resources.resource import Resource


def calculate_geyser_average_production(geyser: Geyser) -> Resource:
    """Calculate average production"""
    average_production = (
        geyser.output_element
        * geyser.eruption_time
        / geyser.eruption_period
        * geyser.activity_time
        / geyser.activity_period
    )
    return average_production
