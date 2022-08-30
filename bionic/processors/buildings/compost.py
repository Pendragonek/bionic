"""Compost"""

from typing import List

from bionic.processors import Processor
from bionic.resources import Resource
from bionic.resources.elements import Dirt, PollutedDirt


class Compost(Processor):
    """Compost class"""

    @property
    def resource_consumption_per_unit(self) -> List[Resource]:
        """Resource consumption per unit property"""
        return [PollutedDirt(amount=60000)]

    @property
    def resource_production_per_unit(self) -> List[Resource]:
        """Resource production per unit property"""
        return [Dirt(amount=60000)]
