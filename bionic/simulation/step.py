"""Simulation step."""

from bionic.processors.buildings import Geyser, SteamTurbine
from bionic.resources import ResourceBank


def simulation_step(
    steam_turbine: SteamTurbine,
    geyser: Geyser,
    element_bank: ResourceBank,
    time: int,
) -> None:
    """Make step of the simulation."""
    steam_turbine.process(element_bank)
    geyser.process(element_bank, time)
