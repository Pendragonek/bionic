"""Lavatory"""

from typing import List

from bionic.processors import Processor
from bionic.resources import Resource
from bionic.resources.elements import PollutedWater, Water


class Lavatory(Processor):
    """Lavatory class"""

    @property
    def resource_consumption_per_unit(self) -> List[Resource]:
        """Resource consumption per unit property"""
        return [Water(amount=5000)]

    @property
    def resource_production_per_unit(self) -> List[Resource]:
        """Resource production per unit property"""
        return [PollutedWater(amount=11700)]
