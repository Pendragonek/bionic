"""Tofu."""

from bionic.resources.food.food import Food


class Tofu(Food):
    """Tofu class."""

    @property
    def calories_per_unit(self) -> int:
        """Calories per unit property."""
        return 3600

    @property
    def quality(self) -> int:
        """Quality property."""
        return 2

    @property
    def spoil_time(self) -> int:
        """Spoil time property."""
        return 2
