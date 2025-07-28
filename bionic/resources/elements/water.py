"""Water."""

from bionic.resources.elements.element import Element


class Water(Element):
    """Water class."""

    @property
    def shc(self) -> float:
        """Return SHC of the element."""
        return 4.179
