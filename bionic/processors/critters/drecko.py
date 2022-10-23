"""Drecko"""

from bionic.processors.critters.critter import Critter
from bionic.resources import Resource
from bionic.resources.elements import Phosphorite
from bionic.resources.food import Meat, PinchaPeppernut


class Drecko(Critter):
    """Drecko class"""

    @property
    def diet(self) -> Resource:
        """Diet property"""
        return PinchaPeppernut(amount=4 * 0.09)

    @property
    def excretion(self) -> Resource:
        """Excretion property"""
        return Phosphorite(amount=10000)

    @property
    def max_age(self) -> int:
        """Max age property"""
        return 150

    @property
    def drop(self) -> Resource:
        """Drop property"""
        return Meat(amount=2)
