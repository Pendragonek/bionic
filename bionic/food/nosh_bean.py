"""Nosh Bean"""

from bionic.food.food import Food


class NoshBean(Food):
    """Nosh Bean class"""

    @property
    def calories_per_unit(self) -> int:
        """Return calories per unit of food"""
        return 0

    @property
    def quality(self) -> int:
        """Return quality of food"""
        return 3

    @property
    def spoil_time(self) -> int:
        """Return spoil time of food"""
        return 4
