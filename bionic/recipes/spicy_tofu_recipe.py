"""Spicy tofu recipe"""

from bionic.food.pincha_peppernut import PinchaPeppernut
from bionic.food.spicy_tofu import SpicyTofu
from bionic.food.tofu import Tofu


class TofuRecipe:
    """Spicy tofu recipe class"""

    ingredient_list = [Tofu(1), PinchaPeppernut(1)]
    product = SpicyTofu(1)
