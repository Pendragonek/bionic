"""Pip"""

from bionic.critters.critter import Critter
from bionic.elements.dirt import Dirt
from bionic.resources.lumber import Lumber
from bionic.resources.resource import Resource


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
