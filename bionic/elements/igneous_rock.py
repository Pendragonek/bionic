"""Igneous Rock element"""
from bionic.elements.element import Element


class IgneousRock(Element):
    """Igneous Rock element class"""

    @property
    def name(self) -> str:
        """Return name of Igneous Rock element"""
        return "Igneous Rock"

    @property
    def shc(self) -> float:
        """Return SHC of Igneous Rock element"""
        return 1.000
