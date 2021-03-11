"""Entity bank"""
from typing import List, Optional, Dict

from bionic.dataclasses.entity import Entity
from bionic.elements import Element


class EntityBank:
    """Entity bank"""

    def __init__(self, entity_list: Optional[List[Entity]] = None):
        self.entity_dict: Dict[str, Entity] = {}

        if entity_list is None:
            return

        for entity in entity_list:
            self.entity_dict[entity.key] = entity

    def get(self, element: Element) -> Entity:
        """Get entity based on element"""
        return self.entity_dict[element.key]
