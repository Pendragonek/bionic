"""Water element"""

from bionic.elements.element import Element


class Water(Element):
    """Water element class"""

    @property
    def name(self) -> str:
        """Return name of Water element"""
        return "Water"

    @property
    def shc(self) -> float:
        """Return SHC of Water element"""
        return 4.179
