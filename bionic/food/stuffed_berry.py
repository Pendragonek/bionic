"""Stuffed berry"""

from bionic.food.food import Food


class StuffedBerry(Food):
    """Stuffed berry class"""

    @property
    def calories_per_unit(self) -> int:
        """Calories per unit property"""
        return 4400

    @property
    def quality(self) -> int:
        """Quality property"""
        return 4

    @property
    def spoil_time(self) -> int:
        """Spoil time property"""
        return 2
