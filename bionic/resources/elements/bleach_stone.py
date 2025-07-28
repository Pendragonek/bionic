"""Bleach stone."""

from bionic.resources.elements.element import Element


class BleachStone(Element):
    """Bleach stone class."""

    @property
    def shc(self) -> float:
        """Return SHC of the element."""
        return 0.500
