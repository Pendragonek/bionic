"""Steam turbine class"""

from bionic.elements.steam import Steam
from bionic.elements.water import Water
from bionic.resources.resource_bank import ResourceBank


class SteamTurbine:
    """Steam turbine class"""

    heat: float = 4

    def process(self, resource_bank: ResourceBank):
        """Process elements"""
        max_mass = 2000
        steam_element = resource_bank.get(Steam)
        if not steam_element.amount or steam_element.temperature < 125:
            return
        if steam_element.amount <= max_mass:
            resource_bank.add(Water(amount=steam_element.amount, temperature=95))
            resource_bank.subtract(steam_element)
        else:
            resource_bank.add(Water(amount=max_mass, temperature=95))
            resource_bank.subtract(
                Steam(amount=max_mass, temperature=steam_element.temperature)
            )
