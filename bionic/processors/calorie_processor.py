"""Calorie processor"""

from abc import abstractmethod
from typing import List

from bionic.processors.processor import Processor
from bionic.resources import Resource
from bionic.resources.food import Food


class CalorieProcessor(Processor):
    """Calorie processor class"""

    @property
    @abstractmethod
    def resource_consumption_per_unit(self) -> List[Resource]:
        """Resource consumption per unit property"""

    @property
    @abstractmethod
    def resource_production_per_unit(self) -> List[Resource]:
        """Resource production per unit property"""

    @property
    def calorie_consumption_per_unit(self) -> float:
        """Calorie consumption per unit property"""
        calorie_consumption = 0
        for consumed_resource in self.resource_consumption_per_unit:
            if isinstance(consumed_resource, Food):
                calorie_consumption += consumed_resource.calories
        return calorie_consumption

    @property
    def calorie_production_per_unit(self) -> float:
        """Calorie production per unit property"""
        calorie_production = 0
        for produced_resource in self.resource_production_per_unit:
            if isinstance(produced_resource, Food):
                calorie_production += produced_resource.calories
        return calorie_production

    @property
    def calorie_consumption(self) -> float:
        """Calorie consumption property"""
        return self.calorie_consumption_per_unit * self.amount

    @property
    def calorie_production(self) -> float:
        """Calorie production property"""
        return self.calorie_production_per_unit * self.amount
