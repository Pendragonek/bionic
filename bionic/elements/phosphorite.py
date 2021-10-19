"""Phosphorite element"""

from bionic.elements.element import Element


class Phosphorite(Element):
    """Phosphorite element class"""

    @property
    def shc(self) -> float:
        """Return SHC of the element"""
        return 0.150
