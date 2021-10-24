"""Tofu recipe"""

from bionic.elements.water import Water
from bionic.food.nosh_bean import NoshBean
from bionic.food.tofu import Tofu


class TofuRecipe:
    """Tofu recipe class"""

    ingredient_list = [NoshBean(6), Water(50000)]
    product = Tofu(1)
