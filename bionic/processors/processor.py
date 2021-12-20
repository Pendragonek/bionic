"""Processor"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from bionic.resources.resource import Resource


@dataclass
class Processor(ABC):
    """Processor class"""

    amount: float = 0

    @property
    @abstractmethod
    def consumption_per_unit(self) -> List[Resource]:
        """Consumption per unit property"""

    @property
    @abstractmethod
    def production_per_unit(self) -> List[Resource]:
        """Production per unit property"""

    @property
    def consumption(self) -> List[Resource]:
        """Consumption property"""
        return [resource * self.amount for resource in self.consumption_per_unit]

    @property
    def production(self) -> List[Resource]:
        """Production property"""
        return [resource * self.amount for resource in self.production_per_unit]
