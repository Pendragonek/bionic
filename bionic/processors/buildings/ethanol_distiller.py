"""Ethanol distiller"""

from typing import List

from bionic.processors import Processor
from bionic.resources import Lumber, Resource
from bionic.resources.elements import CarbonDioxide, Ethanol, PollutedDirt


class EthanolDistiller(Processor):
    """Ethanol distiller class"""

    @property
    def resource_consumption_per_unit(self) -> List[Resource]:
        """Resource consumption per unit property"""
        return [Lumber(amount=600000)]

    @property
    def resource_production_per_unit(self) -> List[Resource]:
        """Resource production per unit property"""
        return [
            Ethanol(amount=300000),
            PollutedDirt(amount=200000),
            CarbonDioxide(amount=100000),
        ]
