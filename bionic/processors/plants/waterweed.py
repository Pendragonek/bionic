"""Waterweed"""

from bionic.processors.plants.plant import Plant
from bionic.resources import Resource
from bionic.resources.elements import SaltWater
from bionic.resources.elements.bleach_stone import BleachStone
from bionic.resources.food import Lettuce


class Waterweed(Plant):
    """Waterweed class"""

    @property
    def growth_speed(self) -> int:
        """Return growth of the plant"""
        return 48

    @property
    def irrigation(self) -> Resource:
        """Return irrigation per cycle of the plant"""
        return SaltWater(amount=5000)

    @property
    def fertilizer(self) -> Resource:
        """Return fertilizer per cycle of the plant"""
        return BleachStone(amount=500)

    @property
    def crop(self) -> Resource:
        """Return crop of the plant"""
        return Lettuce(amount=12)
