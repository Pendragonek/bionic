"""Tofu"""

from bionic.food.food import Food


class Tofu(Food):
    """Tofu class"""

    @property
    def calories_per_unit(self) -> int:
        """Return calories per unit of food"""
        return 3600

    @property
    def quality(self) -> int:
        """Return quality of food"""
        return 2

    @property
    def spoil_time(self) -> int:
        """Return spoil time of food"""
        return 2
