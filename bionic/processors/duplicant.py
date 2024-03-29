"""Duplicant"""

from typing import List

from bionic.processors.calorie_processor import CalorieProcessor
from bionic.resources import Resource
from bionic.resources.elements import CarbonDioxide, Oxygen


class Duplicant(CalorieProcessor):
    """Duplicant class"""

    @property
    def resource_consumption_per_unit(self) -> List[Resource]:
        """Resource consumption per unit property"""
        return [Oxygen(amount=60000)]

    @property
    def resource_production_per_unit(self) -> List[Resource]:
        """Resource production per unit property"""
        return [CarbonDioxide(amount=1200)]

    @property
    def calorie_consumption_per_unit(self) -> float:
        """Calorie consumption per unit property"""
        return 1000

    @property
    def calorie_production_per_unit(self) -> float:
        """Calorie production per unit property"""
        return 0
