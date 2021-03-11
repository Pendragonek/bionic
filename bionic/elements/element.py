"""Element dataclass"""
from dataclasses import dataclass


@dataclass
class Element:
    """Element dataclass"""
    name: str
    shc: float

    @property
    def key(self) -> str:
        """Return key of element"""
        return self.name.lower().replace(" ", "_")
