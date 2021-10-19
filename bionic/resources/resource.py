"""Resource"""
from abc import ABC
from copy import copy
from dataclasses import dataclass
from typing import Union


@dataclass
class Resource(ABC):
    """Resource class"""

    amount: float = 0

    def __mul__(self, other: Union[float, int]) -> "Resource":
        element_copy = copy(self)
        element_copy.amount *= other
        return element_copy

    def __truediv__(self, other: Union[float, int]) -> "Resource":
        element_copy = copy(self)
        element_copy.amount /= other
        return element_copy
