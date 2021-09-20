"""Hydrogen element"""

from bionic.elements.element import Element


class Hydrogen(Element):
    """Hydrogen element class"""

    @property
    def name(self) -> str:
        """Return name of Hydrogen element"""
        return "Hydrogen"

    @property
    def shc(self) -> float:
        """Return SHC of Hydrogen element"""
        return 2.400
