"""Duplicant"""

from typing import List

from bionic.elements.carbon_dioxide import CarbonDioxide
from bionic.elements.oxygen import Oxygen
from bionic.processors.calorie_processor import CalorieProcessor
from bionic.resources.resource import Resource


class Duplicant(CalorieProcessor):
    """Duplicant class"""

    @property
    def consumption_per_unit(self) -> List[Resource]:
        """Consumption per unit property"""
        return [Oxygen(60000)]

    @property
    def production_per_unit(self) -> List[Resource]:
        """Production per unit property"""
        return [CarbonDioxide(1200)]

    @property
    def calories_per_unit(self) -> float:
        """Calorie intake property"""
        return -1000
