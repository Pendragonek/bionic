"""Test compound"""

from typing import List

import pytest

from bionic.compound import Compound
from bionic.elements.water import Water
from bionic.food.nosh_bean import NoshBean
from bionic.food.pincha_peppernut import PinchaPeppernut
from bionic.food.spicy_tofu import SpicyTofu
from bionic.food.tofu import Tofu
from bionic.processors.processor import Processor
from bionic.recipes.spicy_tofu_recipe import SpicyTofuRecipe
from bionic.recipes.tofu_recipe import TofuRecipe
from bionic.resources.resource import Resource
from bionic.resources.resource_bank import ResourceBank


@pytest.mark.parametrize(
    "part_list, expected_consumption, expected_production",
    [
        (
            [TofuRecipe(1)],
            [NoshBean(6), Water(50000)],
            [Tofu(1)],
        ),
        (
            [TofuRecipe(1), SpicyTofuRecipe(1)],
            [NoshBean(6), Water(50000), PinchaPeppernut(1)],
            [SpicyTofu(1)],
        ),
    ],
)
def test_compound_balance(
    part_list: List[Processor],
    expected_consumption: List[Resource],
    expected_production: List[Resource],
):
    """Test compound balance"""
    compound = Compound(part_list)
    expected_consumption_bank = ResourceBank(*expected_consumption)
    expected_production_bank = ResourceBank(*expected_production)
    assert compound.consumption.resource_dict == expected_consumption_bank.resource_dict
    assert compound.production.resource_dict == expected_production_bank.resource_dict
