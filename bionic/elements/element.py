"""Element"""
from abc import ABC, abstractmethod
from copy import copy
from dataclasses import dataclass
from typing import Union


@dataclass  # type: ignore
class Element(ABC):
    """Element class"""

    mass: float = 0
    temperature: float = 0

    @property
    @abstractmethod
    def name(self) -> str:
        """Return name of element"""

    @property
    @abstractmethod
    def shc(self) -> float:
        """Return SHC of element"""

    @property
    def heat(self) -> float:
        """Return heat amount"""
        return self.shc * self.mass * self.temperature

    def __add__(self, other: "Element") -> "Element":
        element_type = type(self)
        if not isinstance(other, element_type):
            raise TypeError
        mass = self.mass + other.mass
        temperature = (
                          self.mass * self.temperature + other.mass * other.temperature
                      ) / mass
        return element_type(mass, temperature)

    def __mul__(self, other: Union[float, int]) -> "Element":
        element_copy = copy(self)
        element_copy.mass *= other
        return element_copy

    def __truediv__(self, other: Union[float, int]) -> "Element":
        element_copy = copy(self)
        element_copy.mass /= other
        return element_copy
