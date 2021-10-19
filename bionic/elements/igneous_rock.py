"""Igneous Rock element"""

from bionic.elements.element import Element


class IgneousRock(Element):
    """Igneous Rock element class"""

    @property
    def shc(self) -> float:
        """Return SHC of element"""
        return 1.000
