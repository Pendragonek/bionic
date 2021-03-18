"""Element class"""
from dataclasses import dataclass


@dataclass
class Element:
    """Element class"""
    name: str
    shc: float

    @property
    def key(self) -> str:
        """Return key of element"""
        return self.name.lower().replace(" ", "_")
