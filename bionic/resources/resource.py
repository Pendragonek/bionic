"""Resource"""

from abc import ABC
from copy import copy
from typing import Union

from pydantic import BaseModel


class Resource(BaseModel, ABC):
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

    def __neg__(self) -> "Resource":
        resource_copy = copy(self)
        resource_copy.amount = -resource_copy.amount
        return resource_copy
