"""Entity bank"""
from typing import Dict

from bionic.elements import Element
from bionic.entities import Entity
from bionic.entities.entity import calculate_combined_entity_temperature


class EntityBank:
    """Entity bank class"""

    def __init__(self, *args: Entity):
        self.entity_dict: Dict[str, Entity] = {}
        for entity in args:
            self.add(entity)

    def get(self, element: Element) -> Entity:
        """Get entity based on element"""
        return self.entity_dict.get(element.key) or Entity(element)

    def add(self, entity: Entity):
        """Add entity to bank"""
        if entity.key in self.entity_dict:
            stored_entity = self.entity_dict[entity.key]
            stored_entity.temperature = calculate_combined_entity_temperature(stored_entity, entity)
            stored_entity.mass += entity.mass
        else:
            self.entity_dict[entity.key] = entity

    def remove(self, entity: Entity):
        """Remove entity from bank"""
        stored_entity = self.get(entity.element)
        if stored_entity.mass < entity.mass:
            raise ArithmeticError
        if stored_entity.mass == 0:
            return
        stored_entity.mass -= entity.mass
