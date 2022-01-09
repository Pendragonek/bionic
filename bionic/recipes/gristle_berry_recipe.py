"""Gristle berry recipe"""

from typing import List

from bionic.food.bristle_berry import BristleBerry
from bionic.food.food import Food
from bionic.food.gristle_berry import GristleBerry
from bionic.recipes.recipe import Recipe
from bionic.resources.resource import Resource


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
