"""Plant"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from bionic.resources.resource import Resource


@dataclass  # type: ignore
class Plant(ABC):
    """Plant class"""

    domesticated: bool = False

    @property
    @abstractmethod
    def growth_speed(self) -> int:
        """Return growth of the plant"""

    @property
    @abstractmethod
    def irrigation(self) -> Resource:
        """Return irrigation of the plant"""

    @property
    @abstractmethod
    def fertilizer(self) -> Resource:
        """Return fertilizer of the plant"""

    @property
    @abstractmethod
    def crop(self) -> Resource:
        """Return crop of the plant"""

    @property
    def production_per_cycle(self) -> Resource:
        """Return production per cycle of the plant"""
        base_production = self.crop / self.growth_speed
        if self.domesticated:
            base_production *= 4
        return base_production

    @property
    def consumption_per_cycle(self) -> List[Resource]:
        """Return consumption per cycle of the plant"""
        if self.domesticated:
            return [self.irrigation, self.fertilizer]
        return []
