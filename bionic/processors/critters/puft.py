"""Puft"""

from bionic.processors.critters.critter import Critter
from bionic.resources import Resource
from bionic.resources.elements import Chlorine, PollutedOxygen, Slime
from bionic.resources.elements.bleach_stone import BleachStone
from bionic.resources.food import Meat


class Puft(Critter):
    """Puft class"""

    @property
    def diet(self) -> Resource:
        """Diet property"""
        return PollutedOxygen(amount=50000)

    @property
    def excretion(self) -> Resource:
        """Excretion property"""
        return Slime(amount=47500)

    @property
    def max_age(self) -> int:
        """Max age property"""
        return 75

    @property
    def drop(self) -> Resource:
        """Drop property"""
        return Meat(amount=1)


class SqueakyPuft(Puft):
    """Squeaky puft class"""

    @property
    def diet(self) -> Resource:
        """Diet property"""
        return Chlorine(amount=30000)

    @property
    def excretion(self) -> Resource:
        """Excretion property"""
        return BleachStone(amount=28500)
