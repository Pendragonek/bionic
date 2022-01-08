"""Critter"""

from abc import abstractmethod
from typing import List

from bionic.processors.processor import Processor
from bionic.resources.resource import Resource


class Critter(Processor):
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
    def resource_production_per_unit(self) -> List[Resource]:
        """Resource production per unit property"""
        base_production = self.excretion
        if not self.tamed:
            base_production /= 4
        return [base_production]

    @property
    def resource_consumption_per_unit(self) -> List[Resource]:
        """Resource consumption per unit property"""
        base_consumption = self.diet
        if not self.tamed:
            base_consumption /= 4
        return [base_consumption]
