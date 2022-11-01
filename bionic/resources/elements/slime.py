"""Slime"""

from bionic.resources.elements.element import Element


class Slime(Element):
    """Slime class"""

    @property
    def shc(self) -> float:
        """Return SHC of the element"""
        return 0.200
