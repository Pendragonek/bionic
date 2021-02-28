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
    def name(self) -> str:
        """Return name of entity element"""
        return self.element.name

    @property
    def shc(self) -> float:
        """Return SHC of entity element"""
        return self.element.shc

    @property
    def heat(self) -> float:
        """Return heat amount"""
        return calculate_heat_amount(self.element.shc, self.mass, self.temperature)


def calculate_combined_entity_temperature(*entity_list: Entity) -> float:
    """Calculate combined temperature of two entities"""
    total_heat = 0.0
    total_heat_capacity = 0.0
    for entity in entity_list:
        total_heat += entity.heat
        total_heat_capacity += entity.shc * entity.mass
    return total_heat / total_heat_capacity
