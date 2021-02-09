"""Entity class"""
from dataclasses import dataclass

from bionic.dataclasses import Element
from bionic.heat import calculate_heat_amount


@dataclass
class Entity:
    """ Entity class"""
    element: Element
    mass: float
    temperature: float

    @property
    def heat(self) -> float:
        """Return heat amount"""
        return calculate_heat_amount(self.element.shc, self.mass, self.temperature)
