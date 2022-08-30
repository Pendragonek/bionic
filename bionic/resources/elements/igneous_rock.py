"""Igneous rock"""

from bionic.resources.elements.element import Element


class IgneousRock(Element):
    """Igneous rock class"""

    @property
    def shc(self) -> float:
        """Return SHC of the element"""
        return 1.000
