"""Bristle blossom"""

from typing import Optional

from bionic.processors.plants.plant import Plant
from bionic.resources import Resource
from bionic.resources.elements import Water
from bionic.resources.food import BristleBerry


class BristleBlossom(Plant):
    """Bristle blossom class"""

    @property
    def growth_speed(self) -> int:
        """Return growth of the plant"""
        return 24

    @property
    def irrigation(self) -> Resource:
        """Return irrigation per cycle of the plant"""
        return Water(amount=20000)

    @property
    def fertilizer(self) -> Optional[Resource]:
        """Return fertilizer per cycle of the plant"""
        return None

    @property
    def crop(self) -> Resource:
        """Return crop of the plant"""
        return BristleBerry(amount=1)
