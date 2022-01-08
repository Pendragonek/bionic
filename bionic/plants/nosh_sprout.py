"""Nosh sprout"""

from bionic.elements.dirt import Dirt
from bionic.elements.ethanol import Ethanol
from bionic.food.nosh_bean import NoshBean
from bionic.plants.plant import Plant
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
