"""Production"""

from bionic.buildings import Geyser
from bionic.elements import Element


def calculate_geyser_average_production(geyser: Geyser) -> Element:
    """Calculate average production"""
    average_production = (
        geyser.output_element
        * geyser.eruption_time
        / geyser.eruption_period
        * geyser.activity_time
        / geyser.activity_period
    )
    return average_production
