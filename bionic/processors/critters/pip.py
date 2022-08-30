"""Pip"""

from bionic.processors.critters.critter import Critter
from bionic.resources import Lumber, Resource
from bionic.resources.elements import Dirt


class Pip(Critter):
    """Pip class"""

    @property
    def diet(self) -> Resource:
        """Diet property"""
        return Lumber(amount=135000)

    @property
    def excretion(self) -> Resource:
        """Excretion property"""
        return Dirt(amount=20000)
