"""Processor."""

from abc import ABC, abstractmethod

from pydantic import BaseModel

from bionic.resources import Resource


class Processor(BaseModel, ABC):
    """Processor class."""

    amount: float = 0

    @property
    @abstractmethod
    def resource_consumption_per_unit(self) -> list[Resource]:
        """Resource consumption per unit property."""

    @property
    @abstractmethod
    def resource_production_per_unit(self) -> list[Resource]:
        """Resource production per unit property."""

    @property
    def resource_consumption(self) -> list[Resource]:
        """Resource consumption property."""
        return [
            resource * self.amount for resource in self.resource_consumption_per_unit
        ]

    @property
    def resource_production(self) -> list[Resource]:
        """Resource production property."""
        return [
            resource * self.amount for resource in self.resource_production_per_unit
        ]
