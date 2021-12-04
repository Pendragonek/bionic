"""Ethanol"""

from bionic.elements.element import Element


class Ethanol(Element):
    """Ethanol class"""

    @property
    def shc(self) -> float:
        """Return SHC of the element"""
        return 2.460
