"""Polluted water element"""

from bionic.elements.element import Element


class PollutedWater(Element):
    """Polluted water element class"""

    @property
    def shc(self) -> float:
        """Return SHC of the element"""
        return 4.179
