"""Polluted dirt"""

from bionic.resources.elements.element import Element


class PollutedDirt(Element):
    """Polluted dirt class"""

    @property
    def shc(self) -> float:
        """Return SHC of the element"""
        return 0.830
