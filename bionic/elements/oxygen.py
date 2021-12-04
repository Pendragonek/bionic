"""Oxygen"""

from bionic.elements.element import Element


class Oxygen(Element):
    """Oxygen class"""

    @property
    def shc(self) -> float:
        """Return SHC of the element"""
        return 1.005
