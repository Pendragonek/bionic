"""Steam."""

from bionic.resources.elements.element import Element


class Steam(Element):
    """Steam class."""

    @property
    def shc(self) -> float:
        """Return SHC of the element."""
        return 4.179
