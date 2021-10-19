"""Pincha pepper"""

from bionic.elements.phosphorite import Phosphorite
from bionic.elements.polluted_water import PollutedWater
from bionic.food.pincha_peppernut import PinchaPeppernut
from bionic.plants.plant import Plant
from bionic.resources.resource import Resource


class PinchaPepper(Plant):
    """Pincha pepper class"""

    @property
    def growth_speed(self) -> int:
        """Return growth of the plant"""
        return 32

    @property
    def irrigation(self) -> Resource:
        """Return irrigation per cycle of the plant"""
        return PollutedWater(35000)

    @property
    def fertilizer(self) -> Resource:
        """Return fertilizer per cycle of the plant"""
        return Phosphorite(1000)

    @property
    def crop(self) -> Resource:
        """Return crop of the plant"""
        return PinchaPeppernut(4)
