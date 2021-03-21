"""Element"""
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Element(ABC):
    """Element class"""
    mass: float = 0
    temperature: float = 0

    @property
    @abstractmethod
    def name(self) -> str:
        """Return name of element"""
        pass

    @property
    @abstractmethod
    def shc(self) -> float:
        """Return SHC of element"""
        pass

    @property
    def heat(self) -> float:
        """Return heat amount"""
        return self.shc * self.mass * self.temperature
