"""Hydrogen"""

from bionic.elements.element import Element


class Hydrogen(Element):
    """Hydrogen class"""

    @property
    def shc(self) -> float:
        """Return SHC of element"""
        return 2.400
