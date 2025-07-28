"""Stuffed berry recipe."""

from bionic.processors.recipes.recipe import Recipe
from bionic.resources import Resource
from bionic.resources.food import Food, GristleBerry, PinchaPeppernut, StuffedBerry


class StuffedBerryRecipe(Recipe):
    """Stuffed berry recipe class."""

    @property
    def ingredient_list(self) -> list[Resource]:
        """Ingredient list property."""
        return [GristleBerry(amount=2), PinchaPeppernut(amount=2)]

    @property
    def product(self) -> Food:
        """Product property."""
        return StuffedBerry(amount=1)
