"""Simulation step"""

from bionic.buildings.geyser import Geyser
from bionic.buildings.steam_turbine import SteamTurbine
from bionic.entities import EntityBank


def simulation_step(steam_turbine: SteamTurbine, geyser: Geyser, entity_bank: EntityBank, time: int):
    """Make step of the simulation"""
    steam_turbine.process(entity_bank)
    geyser.process(entity_bank, time)
