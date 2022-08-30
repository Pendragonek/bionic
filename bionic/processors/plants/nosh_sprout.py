"""Nosh sprout"""

from bionic.processors.plants.plant import Plant
from bionic.resources.elements import Dirt, Ethanol
from bionic.resources.food import NoshBean
from bionic.resources.resource import Resource


class NoshSprout(Plant):
    """Nosh sprout class"""

    @property
    def growth_speed(self) -> int:
        """Return growth of the plant"""
        return 84

    @property
    def irrigation(self) -> Resource:
        """Return irrigation per cycle of the plant"""
        return Ethanol(amount=20000)

    @property
    def fertilizer(self) -> Resource:
        """Return fertilizer per cycle of the plant"""
        return Dirt(amount=5000)

    @property
    def crop(self) -> Resource:
        """Return crop of the plant"""
        return NoshBean(amount=12)
