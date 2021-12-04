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
    def consumption(self) -> List[Resource]:
        """Consumption property"""

    @property
    @abstractmethod
    def production(self) -> List[Resource]:
        """Production property"""
