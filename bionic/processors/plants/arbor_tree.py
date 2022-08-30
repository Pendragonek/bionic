"""Arbor tree"""

from bionic.processors.plants.plant import Plant
from bionic.resources import Lumber, Resource
from bionic.resources.elements import Dirt, PollutedWater


class ArborTree(Plant):
    """Arbor tree class"""

    @property
    def growth_speed(self) -> int:
        """Return growth of the plant"""
        return 18

    @property
    def irrigation(self) -> Resource:
        """Return irrigation per cycle of the plant"""
        return PollutedWater(amount=70000)

    @property
    def fertilizer(self) -> Resource:
        """Return fertilizer per cycle of the plant"""
        return Dirt(amount=10000)

    @property
    def crop(self) -> Resource:
        """Return crop of the plant"""
        return Lumber(amount=1500000)
