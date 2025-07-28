"""Barbeque recipe."""

from bionic.processors.recipes.recipe import Recipe
from bionic.resources import Resource
from bionic.resources.food import Barbeque, Food, Meat


class BarbequeRecipe(Recipe):
    """Barbeque recipe class."""

    @property
    def ingredient_list(self) -> list[Resource]:
        """Ingredient list property."""
        return [Meat(amount=2)]

    @property
    def product(self) -> Food:
        """Product property."""
        return Barbeque(amount=1)
