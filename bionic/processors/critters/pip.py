"""Pip."""

from bionic.processors.critters.critter import Critter
from bionic.resources import Lumber, Resource
from bionic.resources.elements import Dirt
from bionic.resources.food import Meat


class Pip(Critter):
    """Pip class."""

    @property
    def diet(self) -> Resource:
        """Diet property."""
        return Lumber(amount=135000)

    @property
    def excretion(self) -> Resource:
        """Excretion property."""
        return Dirt(amount=20000)

    @property
    def max_age(self) -> int:
        """Max age property."""
        return 100

    @property
    def drop(self) -> Resource:
        """Drop property."""
        return Meat(amount=1)
