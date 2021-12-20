"""Food"""

from abc import abstractmethod

from bionic.resources.resource import Resource


class Food(Resource):
    """Food class"""

    @property
    @abstractmethod
    def calories_per_unit(self) -> float:
        """Calories per unit property"""

    @property
    @abstractmethod
    def quality(self) -> int:
        """Quality property"""

    @property
    @abstractmethod
    def spoil_time(self) -> int:
        """Spoil time property"""

    @property
    def calories(self) -> float:
        """Calories property"""
        return self.calories_per_unit * self.amount
