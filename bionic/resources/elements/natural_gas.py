"""Natural gas"""

from bionic.resources.elements.element import Element


class NaturalGas(Element):
    """Natural gas class"""

    @property
    def shc(self) -> float:
        """Return SHC of the element"""
        return 2.191
