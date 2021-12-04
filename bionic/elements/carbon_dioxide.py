"""Carbon dioxide"""

from bionic.elements.element import Element


class CarbonDioxide(Element):
    """Carbon dioxide class"""

    @property
    def shc(self) -> float:
        """Return SHC of the element"""
        return 0.846
