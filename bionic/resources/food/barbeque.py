"""Barbeque"""

from bionic.resources.food.food import Food


class Barbeque(Food):
    """Barbeque class"""

    @property
    def calories_per_unit(self) -> int:
        """Calories per unit property"""
        return 4000

    @property
    def quality(self) -> int:
        """Quality property"""
        return 3

    @property
    def spoil_time(self) -> int:
        """Spoil time property"""
        return 4
