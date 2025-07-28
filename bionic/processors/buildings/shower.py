"""Shower."""

from bionic.processors import Processor
from bionic.resources import Resource
from bionic.resources.elements import PollutedWater, Water


class Shower(Processor):
    """Shower class."""

    @property
    def resource_consumption_per_unit(self) -> list[Resource]:
        """Resource consumption per unit property."""
        return [Water(amount=16000)]

    @property
    def resource_production_per_unit(self) -> list[Resource]:
        """Resource production per unit property."""
        return [PollutedWater(amount=16000)]
