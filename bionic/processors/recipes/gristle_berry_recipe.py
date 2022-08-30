"""Gristle berry recipe"""

from typing import List

from bionic.processors.recipes.recipe import Recipe
from bionic.resources import Resource
from bionic.resources.food import BristleBerry, Food, GristleBerry


class GristleBerryRecipe(Recipe):
    """Gristle berry recipe class"""

    @property
    def ingredient_list(self) -> List[Resource]:
        """Ingredient list property"""
        return [BristleBerry(amount=1)]

    @property
    def product(self) -> Food:
        """Product property"""
        return GristleBerry(amount=1)
