"""Entity class"""
from dataclasses import dataclass

from bionic.dataclasses import Element
from bionic.heat import calculate_heat_amount, calculate_combined_temperature


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


def calculate_combined_entity_temperature(entity1: Entity, entity2: Entity) -> float:
    """Calculate combined temperature of two entities"""
    return calculate_combined_temperature(entity1.shc, entity1.mass, entity1.temperature,
                                          entity2.shc, entity2.mass, entity2.temperature)
