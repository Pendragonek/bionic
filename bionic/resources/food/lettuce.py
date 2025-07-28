"""Lettuce."""

from bionic.resources.food.food import Food


class Lettuce(Food):
    """Lettuce class."""

    @property
    def calories_per_unit(self) -> int:
        """Calories per unit property."""
        return 400

    @property
    def quality(self) -> int:
        """Quality property."""
        return 0

    @property
    def spoil_time(self) -> int:
        """Spoil time property."""
        return 4
