"""Ethanol distiller"""

from typing import List

from bionic.elements.carbon_dioxide import CarbonDioxide
from bionic.elements.ethanol import Ethanol
from bionic.elements.polluted_dirt import PollutedDirt
from bionic.processors.processor import Processor
from bionic.resources.lumber import Lumber
from bionic.resources.resource import Resource


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
