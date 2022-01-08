"""Calorie processor"""

from abc import abstractmethod

from bionic.processors.processor import Processor


class CalorieProcessor(Processor):
    """Calorie processor class"""

    @property
    @abstractmethod
    def calorie_consumption_per_unit(self) -> float:
        """Calories per unit property"""

    @property
    @abstractmethod
    def calorie_production_per_unit(self) -> float:
        """Calories per unit property"""

    @property
    def calorie_consumption(self) -> float:
        """Calorie consumption property"""
        return self.calorie_consumption_per_unit * self.amount

    @property
    def calorie_production(self) -> float:
        """Calorie production property"""
        return self.calorie_production_per_unit * self.amount
