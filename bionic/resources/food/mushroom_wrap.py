"""Mushroom wrap."""

from bionic.resources.food.food import Food


class MushroomWrap(Food):
    """Mushroom wrap class."""

    @property
    def calories_per_unit(self) -> int:
        """Calories per unit property."""
        return 4800

    @property
    def quality(self) -> int:
        """Quality property."""
        return 4

    @property
    def spoil_time(self) -> int:
        """Spoil time property."""
        return 4
