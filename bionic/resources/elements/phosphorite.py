"""Phosphorite"""

from bionic.resources.elements.element import Element


class Phosphorite(Element):
    """Phosphorite class"""

    @property
    def shc(self) -> float:
        """Return SHC of the element"""
        return 0.150
