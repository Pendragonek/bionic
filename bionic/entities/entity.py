"""Entity class"""
from dataclasses import dataclass

from bionic.calculations.heat import calculate_heat_amount
from bionic.elements import Element


@dataclass
class Entity:
    """ Entity class"""
    element: Element
    mass: float = 0
    temperature: float = 0

    @property
    def name(self) -> str:
        """Return name of entity element"""
        return self.element.name

    @property
    def key(self) -> str:
        """Return key of entity element"""
        return self.element.key

    @property
    def shc(self) -> float:
        """Return SHC of entity element"""
        return self.element.shc

    @property
    def heat(self) -> float:
        """Return calculations amount"""
        return calculate_heat_amount(self.element.shc, self.mass, self.temperature)


def calculate_combined_entity_temperature(*entity_list: Entity) -> float:
    """Calculate combined temperature of two entities"""
    total_heat = 0.0
    total_heat_capacity = 0.0
    for entity in entity_list:
        total_heat += entity.heat
        total_heat_capacity += entity.shc * entity.mass
    return total_heat / total_heat_capacity
