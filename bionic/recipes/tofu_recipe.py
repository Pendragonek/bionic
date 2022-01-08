"""Tofu recipe"""

from typing import List

from bionic.elements.water import Water
from bionic.food.food import Food
from bionic.food.nosh_bean import NoshBean
from bionic.food.tofu import Tofu
from bionic.recipes.recipe import Recipe
from bionic.resources.resource import Resource


class TofuRecipe(Recipe):
    """Tofu recipe class"""

    @property
    def ingredient_list(self) -> List[Resource]:
        """Ingredient list property"""
        return [NoshBean(amount=6), Water(amount=50000)]

    @property
    def product(self) -> Food:
        """Product property"""
        return Tofu(amount=1)
