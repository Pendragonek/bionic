"""Processor"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from bionic.resources.resource import Resource


@dataclass  # type: ignore
class Processor(ABC):
    """Processor class"""

    amount: float = 0

    @property
    @abstractmethod
    def resource_consumption_per_unit(self) -> List[Resource]:
        """Resource consumption per unit property"""

    @property
    @abstractmethod
    def resource_production_per_unit(self) -> List[Resource]:
        """Resource production per unit property"""

    @property
    def resource_consumption(self) -> List[Resource]:
        """Resource consumption property"""
        return [
            resource * self.amount for resource in self.resource_consumption_per_unit
        ]

    @property
    def resource_production(self) -> List[Resource]:
        """Resource production property"""
        return [
            resource * self.amount for resource in self.resource_production_per_unit
        ]
