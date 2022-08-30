"""Gristle berry"""

from bionic.resources.food.food import Food


class GristleBerry(Food):
    """Gristle berry class"""

    @property
    def calories_per_unit(self) -> int:
        """Calories per unit property"""
        return 2000

    @property
    def quality(self) -> int:
        """Quality property"""
        return 1

    @property
    def spoil_time(self) -> int:
        """Spoil time property"""
        return 8
