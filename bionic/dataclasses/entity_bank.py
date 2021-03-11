"""Entity bank"""
from typing import Dict

from bionic.dataclasses.entity import Entity
from bionic.elements import Element


class EntityBank:
    """Entity bank"""

    def __init__(self, *args: Entity):
        self.entity_dict: Dict[str, Entity] = {}
        for entity in args:
            self.entity_dict[entity.key] = entity

    def get(self, element: Element) -> Entity:
        """Get entity based on element"""
        return self.entity_dict.get(element.key) or Entity(element)
