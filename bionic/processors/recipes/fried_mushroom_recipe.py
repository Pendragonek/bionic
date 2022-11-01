"""Fried mushroom recipe"""

from typing import List

from bionic.processors.recipes.recipe import Recipe
from bionic.resources import Resource
from bionic.resources.food import Food, FriedMushroom, Mushroom


class FriedMushroomRecipe(Recipe):
    """Fried mushroom recipe class"""

    @property
    def ingredient_list(self) -> List[Resource]:
        """Ingredient list property"""
        return [Mushroom(amount=1)]

    @property
    def product(self) -> Food:
        """Product property"""
        return FriedMushroom(amount=1)
