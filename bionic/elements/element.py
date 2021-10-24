"""Element"""

from abc import abstractmethod
from dataclasses import dataclass

from bionic.resources.resource import Resource


@dataclass  # type: ignore
class Element(Resource):
    """Element class"""

    temperature: float = 0

    @property
    @abstractmethod
    def shc(self) -> float:
        """Return SHC of the element"""

    @property
    def heat(self) -> float:
        """Return heat amount"""
        return self.shc * self.amount * self.temperature

    def __add__(self, other: "Element") -> "Element":
        element_type = type(self)
        if not isinstance(other, element_type):
            raise TypeError
        mass = self.amount + other.amount
        temperature = (
            self.amount * self.temperature + other.amount * other.temperature
        ) / mass
        return element_type(mass, temperature)
