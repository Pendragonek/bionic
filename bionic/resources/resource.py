"""Resource"""

from abc import ABC
from copy import copy
from dataclasses import dataclass
from typing import Union


@dataclass
class Resource(ABC):
    """Resource class"""

    amount: float = 0

    def __add__(self, other: "Resource") -> "Resource":
        resource_copy = copy(self)
        resource_copy.amount += other.amount
        return resource_copy

    def __sub__(self, other: "Resource") -> "Resource":
        resource_copy = copy(self)
        resource_copy.amount -= other.amount
        return resource_copy

    def __mul__(self, other: Union[float, int]) -> "Resource":
        resource_copy = copy(self)
        resource_copy.amount *= other
        return resource_copy

    def __truediv__(self, other: Union[float, int]) -> "Resource":
        resource_copy = copy(self)
        resource_copy.amount /= other
        return resource_copy
