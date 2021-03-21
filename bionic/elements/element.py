"""Element class"""
from abc import ABC, abstractmethod
from dataclasses import dataclass

from bionic.calculations.heat import calculate_heat_amount


@dataclass
class Element(ABC):
    """Element class"""
    mass: float = 0
    temperature: float = 0

    @property
    @abstractmethod
    def name(self) -> str:
        """Return name of element"""
        pass

    @property
    @abstractmethod
    def shc(self) -> float:
        """Return SHC of element"""
        pass

    @property
    def heat(self) -> float:
        """Return calculations amount"""
        return calculate_heat_amount(self.shc, self.mass, self.temperature)


def calculate_combined_element_temperature(*element_list: Element) -> float:
    """Calculate combined temperature of two entities"""
    total_heat = 0.0
    total_heat_capacity = 0.0
    for element in element_list:
        total_heat += element.heat
        total_heat_capacity += element.shc * element.mass
    return total_heat / total_heat_capacity
