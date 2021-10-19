"""Spicy tofu"""
from bionic.food.food import Food


class SpicyTofu(Food):
    """Spicy tofu class"""

    @property
    def calories_per_unit(self) -> int:
        """Return calories per unit of food"""
        return 4000

    @property
    def quality(self) -> int:
        """Return quality of food"""
        return 5

    @property
    def spoil_time(self) -> int:
        """Return spoil time of food"""
        return 2
