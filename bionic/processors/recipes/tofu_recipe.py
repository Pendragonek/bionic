"""Tofu recipe."""

from bionic.processors.recipes.recipe import Recipe
from bionic.resources import Resource
from bionic.resources.elements import Water
from bionic.resources.food import Food, NoshBean, Tofu


class TofuRecipe(Recipe):
    """Tofu recipe class."""

    @property
    def ingredient_list(self) -> list[Resource]:
        """Ingredient list property."""
        return [NoshBean(amount=6), Water(amount=50000)]

    @property
    def product(self) -> Food:
        """Product property."""
        return Tofu(amount=1)
