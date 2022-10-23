"""Critter"""

from abc import abstractmethod
from typing import List

from bionic.processors import CalorieProcessor
from bionic.resources import Resource


class Critter(CalorieProcessor):
    """Critter class"""

    tamed: bool = False

    @property
    @abstractmethod
    def diet(self) -> Resource:
        """Diet property"""

    @property
    @abstractmethod
    def excretion(self) -> Resource:
        """Excretion property"""

    @property
    @abstractmethod
    def max_age(self) -> int:
        """Max age property"""

    @property
    @abstractmethod
    def drop(self) -> Resource:
        """Drop property"""

    @property
    def resource_production_per_unit(self) -> List[Resource]:
        """Resource production per unit property"""
        base_production = self.excretion
        if not self.tamed:
            base_production /= 4
        return [base_production, self.drop / self.max_age]

    @property
    def resource_consumption_per_unit(self) -> List[Resource]:
        """Resource consumption per unit property"""
        base_consumption = self.diet
        if not self.tamed:
            base_consumption /= 4
        return [base_consumption]
