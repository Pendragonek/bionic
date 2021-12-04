"""Duplicant"""

from typing import List

from bionic.elements.carbon_dioxide import CarbonDioxide
from bionic.elements.oxygen import Oxygen
from bionic.processors.processor import Processor
from bionic.resources.resource import Resource


class Duplicant(Processor):
    """Duplicant class"""

    @property
    def consumption(self) -> List[Resource]:
        """Consumption property"""
        return [Oxygen(60000)]

    @property
    def production(self) -> List[Resource]:
        """Production property"""
        return [CarbonDioxide(1200)]

    @property
    def calories(self) -> float:
        """Calorie intake property"""
        return - 1000 * self.amount

