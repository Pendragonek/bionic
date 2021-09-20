"""Simulation step"""

from bionic.buildings import Geyser, SteamTurbine
from bionic.elements import ElementBank


def simulation_step(
    steam_turbine: SteamTurbine, geyser: Geyser, element_bank: ElementBank, time: int
):
    """Make step of the simulation"""
    steam_turbine.process(element_bank)
    geyser.process(element_bank, time)
