"""Steam turbine class"""

from bionic.resources.resource_bank import ResourceBank
from bionic.elements.steam import Steam
from bionic.elements.water import Water


class SteamTurbine:
    """Steam turbine class"""

    heat: float = 4

    def process(self, element_bank: ResourceBank):
        """Process elements"""
        max_mass = 2000
        steam_element = element_bank.get(Steam)
        if not steam_element.amount or steam_element.temperature < 125:
            return
        if steam_element.amount <= max_mass:
            element_bank.add(Water(steam_element.amount, 95))
            element_bank.remove(steam_element)
        else:
            element_bank.add(Water(max_mass, 95))
            element_bank.remove(Steam(max_mass, steam_element.temperature))
