"""Bristle berry"""

from bionic.food.food import Food


class BristleBerry(Food):
    """Bristle berry class"""

    @property
    def calories_per_unit(self) -> int:
        """Calories per unit property"""
        return 1600

    @property
    def quality(self) -> int:
        """Quality property"""
        return 0

    @property
    def spoil_time(self) -> int:
        """Spoil time property"""
        return 8
