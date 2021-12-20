"""Plant"""

from abc import abstractmethod
from dataclasses import dataclass
from typing import List

from bionic.processors.processor import Processor
from bionic.resources.resource import Resource


@dataclass  # type: ignore
class Plant(Processor):
    """Plant class"""

    domesticated: bool = False

    @property
    @abstractmethod
    def growth_speed(self) -> int:
        """Growth speed property"""

    @property
    @abstractmethod
    def irrigation(self) -> Resource:
        """Irrigation property"""

    @property
    @abstractmethod
    def fertilizer(self) -> Resource:
        """Fertilizer property"""

    @property
    @abstractmethod
    def crop(self) -> Resource:
        """Crop property"""

    @property
    def resource_production_per_unit(self) -> List[Resource]:
        """Resource production per unit property"""
        base_production = self.crop / self.growth_speed
        if self.domesticated:
            base_production *= 4
        return [base_production]

    @property
    def resource_consumption_per_unit(self) -> List[Resource]:
        """Resource consumption per unit property"""
        if self.domesticated:
            return [self.irrigation, self.fertilizer]
        return []
