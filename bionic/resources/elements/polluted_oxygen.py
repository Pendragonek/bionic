"""Polluted oxygen."""

from bionic.resources.elements.element import Element


class PollutedOxygen(Element):
    """Polluted oxygen class."""

    @property
    def shc(self) -> float:
        """Return SHC of the element."""
        return 1.010
