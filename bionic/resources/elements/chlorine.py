"""Chlorine"""

from bionic.resources.elements.element import Element


class Chlorine(Element):
    """Chlorine class"""

    @property
    def shc(self) -> float:
        """Return SHC of the element"""
        return 0.480
