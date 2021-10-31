"""Simulation step"""

from bionic.buildings.geyser import Geyser
from bionic.buildings.steam_turbine import SteamTurbine
from bionic.resources.resource_bank import ResourceBank


def simulation_step(
    steam_turbine: SteamTurbine, geyser: Geyser, element_bank: ResourceBank, time: int
):
    """Make step of the simulation"""
    steam_turbine.process(element_bank)
    geyser.process(element_bank, time)
