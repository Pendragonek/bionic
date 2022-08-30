"""Production"""

from bionic.processors.buildings import Geyser
from bionic.resources import Resource


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
