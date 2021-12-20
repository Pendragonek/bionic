"""Spicy tofu"""

from bionic.food.food import Food


class SpicyTofu(Food):
    """Spicy tofu class"""

    @property
    def calories_per_unit(self) -> int:
        """Calories per unit property"""
        return 4000

    @property
    def quality(self) -> int:
        """Quality property"""
        return 5

    @property
    def spoil_time(self) -> int:
        """Spoil time property"""
        return 2
