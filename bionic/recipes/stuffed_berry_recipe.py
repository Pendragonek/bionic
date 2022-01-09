"""Stuffed berry recipe"""

from typing import List

from bionic.food.food import Food
from bionic.food.gristle_berry import GristleBerry
from bionic.food.pincha_peppernut import PinchaPeppernut
from bionic.food.stuffed_berry import StuffedBerry
from bionic.recipes.recipe import Recipe
from bionic.resources.resource import Resource


class StuffedBerryRecipe(Recipe):
    """Stuffed berry recipe class"""

    @property
    def ingredient_list(self) -> List[Resource]:
        """Ingredient list property"""
        return [GristleBerry(amount=2), PinchaPeppernut(amount=2)]

    @property
    def product(self) -> Food:
        """Product property"""
        return StuffedBerry(amount=1)
