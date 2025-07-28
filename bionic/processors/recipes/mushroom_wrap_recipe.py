"""Mushroom wrap recipe."""

from bionic.processors.recipes.recipe import Recipe
from bionic.resources import Resource
from bionic.resources.food import Food, FriedMushroom, Lettuce, MushroomWrap


class MushroomWrapRecipe(Recipe):
    """Mushroom wrap recipe class."""

    @property
    def ingredient_list(self) -> list[Resource]:
        """Ingredient list property."""
        return [FriedMushroom(amount=1), Lettuce(amount=4)]

    @property
    def product(self) -> Food:
        """Product property."""
        return MushroomWrap(amount=1)
