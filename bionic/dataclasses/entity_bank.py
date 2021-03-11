"""Entity bank"""
from typing import Dict

from bionic.dataclasses.entity import Entity
from bionic.elements import Element


class EntityBank:
    """Entity bank"""

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
            self.entity_dict[entity.key].mass += entity.mass
        else:
            self.entity_dict[entity.key] = entity

    def remove(self, entity: Entity):
        """Remove entity from bank"""
        if entity.key not in self.entity_dict:
            return

        stored_entity = self.entity_dict[entity.key]
        stored_entity.mass -= entity.mass
        if stored_entity.mass < 0:
            self.entity_dict.pop(entity.key)
