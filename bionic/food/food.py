"""Food"""
from abc import abstractmethod

from bionic.resources.resource import Resource


class Food(Resource):
    """Food class"""

    @property
    @abstractmethod
    def calories_per_unit(self) -> int:
        """Return calories per unit of food"""

    @property
    @abstractmethod
    def quality(self) -> int:
        """Return quality of food"""

    @property
    @abstractmethod
    def spoil_time(self) -> int:
        """Return spoil time of food"""

    @property
    def calories(self) -> float:
        """Return calories of food"""
        return self.amount * self.calories_per_unit
