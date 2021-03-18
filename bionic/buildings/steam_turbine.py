"""Steam Turbine class"""

from bionic.elements import STEAM, WATER
from bionic.entities import Entity, EntityBank


class SteamTurbine:
    """Steam turbine class"""

    name: str = "Steam Turbine"
    heat: float = 4

    def process(self, entity_bank: EntityBank):
        """Process elements"""
        max_mass = 2000
        steam_entity = entity_bank.get(STEAM)
        if not steam_entity.mass or steam_entity.temperature < 125:
            return
        if steam_entity.mass <= max_mass:
            entity_bank.add(Entity(WATER, steam_entity.mass, 95))
            entity_bank.remove(steam_entity)
        else:
            entity_bank.add(Entity(WATER, max_mass, 95))
            entity_bank.remove(Entity(STEAM, max_mass, steam_entity.temperature))
