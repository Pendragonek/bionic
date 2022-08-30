"""Dirt"""

from bionic.resources.elements.element import Element


class Dirt(Element):
    """Dirt class"""

    @property
    def name(self) -> str:
        """Return name of Dirt element"""
        return "Dirt"

    @property
    def shc(self) -> float:
        """Return SHC of Dirt element"""
        return 1.480
