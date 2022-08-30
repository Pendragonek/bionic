"""Pincha pepper"""

from bionic.processors.plants.plant import Plant
from bionic.resources import Resource
from bionic.resources.elements import Phosphorite, PollutedWater
from bionic.resources.food import PinchaPeppernut


class PinchaPepper(Plant):
    """Pincha pepper class"""

    @property
    def growth_speed(self) -> int:
        """Return growth of the plant"""
        return 32

    @property
    def irrigation(self) -> Resource:
        """Return irrigation per cycle of the plant"""
        return PollutedWater(amount=35000)

    @property
    def fertilizer(self) -> Resource:
        """Return fertilizer per cycle of the plant"""
        return Phosphorite(amount=1000)

    @property
    def crop(self) -> Resource:
        """Return crop of the plant"""
        return PinchaPeppernut(amount=4)
