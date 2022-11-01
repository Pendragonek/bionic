"""Dusk cap"""

from typing import Optional

from bionic.processors.plants.plant import Plant
from bionic.resources import Resource
from bionic.resources.elements import Slime
from bionic.resources.food import Mushroom


class DuskCap(Plant):
    """Dusk cap class"""

    @property
    def growth_speed(self) -> int:
        """Return growth of the plant"""
        return 30

    @property
    def irrigation(self) -> Optional[Resource]:
        """Return irrigation per cycle of the plant"""
        return None

    @property
    def fertilizer(self) -> Resource:
        """Return fertilizer per cycle of the plant"""
        return Slime(amount=4000)

    @property
    def crop(self) -> Resource:
        """Return crop of the plant"""
        return Mushroom(amount=1)
