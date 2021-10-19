"""Steam element"""

from bionic.elements.element import Element


class Steam(Element):
    """Steam element class"""

    @property
    def shc(self) -> float:
        """Return SHC of the element"""
        return 4.179
