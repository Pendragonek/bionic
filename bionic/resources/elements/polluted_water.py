"""Polluted water"""

from bionic.resources.elements.element import Element


class PollutedWater(Element):
    """Polluted water class"""

    @property
    def shc(self) -> float:
        """Return SHC of the element"""
        return 4.179
