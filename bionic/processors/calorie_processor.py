"""Calorie processor"""

from abc import abstractmethod
from typing import List

from bionic.processors.processor import Processor
from bionic.resources.resource import Resource


class CalorieProcessor(Processor):
    """Calorie processor class"""

    @property
    @abstractmethod
    def consumption_per_unit(self) -> List[Resource]:
        """Consumption per unit property"""

    @property
    @abstractmethod
    def production_per_unit(self) -> List[Resource]:
        """Production per unit property"""

    @property
    @abstractmethod
    def calories_per_unit(self) -> float:
        """Calories per unit property"""

    @property
    def calories(self) -> float:
        """Calories property"""
        return self.calories_per_unit * self.amount
