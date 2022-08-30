"""Spicy tofu recipe"""

from typing import List

from bionic.processors.recipes.recipe import Recipe
from bionic.resources import Resource
from bionic.resources.food import Food, PinchaPeppernut, SpicyTofu, Tofu


class SpicyTofuRecipe(Recipe):
    """Spicy tofu recipe class"""

    @property
    def ingredient_list(self) -> List[Resource]:
        """Ingredient list property"""
        return [Tofu(amount=1), PinchaPeppernut(amount=1)]

    @property
    def product(self) -> Food:
        """Product property"""
        return SpicyTofu(amount=1)
