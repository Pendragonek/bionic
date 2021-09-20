"""Steam element"""

from bionic.elements.element import Element


class Steam(Element):
    """Steam element class"""

    @property
    def name(self) -> str:
        """Return name of Steam element"""
        return "Steam"

    @property
    def shc(self) -> float:
        """Return SHC of Steam element"""
        return 4.179
