"""Salt water."""

from bionic.resources.elements.element import Element


class SaltWater(Element):
    """Salt water class."""

    @property
    def shc(self) -> float:
        """Return SHC of the element."""
        return 4.100
