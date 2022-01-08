"""Spicy tofu recipe"""

from typing import List

from bionic.food.food import Food
from bionic.food.pincha_peppernut import PinchaPeppernut
from bionic.food.spicy_tofu import SpicyTofu
from bionic.food.tofu import Tofu
from bionic.recipes.recipe import Recipe
from bionic.resources.resource import Resource


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
