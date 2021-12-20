"""Test compound"""

from typing import List

import pytest

from bionic.compound import Compound
from bionic.elements.water import Water
from bionic.food.nosh_bean import NoshBean
from bionic.food.pincha_peppernut import PinchaPeppernut
from bionic.food.spicy_tofu import SpicyTofu
from bionic.food.tofu import Tofu
from bionic.plants.nosh_sprout import NoshSprout
from bionic.processors.processor import Processor
from bionic.recipes.spicy_tofu_recipe import SpicyTofuRecipe
from bionic.recipes.tofu_recipe import TofuRecipe
from bionic.resources.resource import Resource
from bionic.resources.resource_bank import ResourceBank


@pytest.mark.parametrize(
    "part_list, expected_consumption, expected_production, expected_calories",
    [
        (
            [TofuRecipe(4)],
            [NoshBean(24), Water(200000)],
            [Tofu(4)],
            14400,
        ),
        (
            [TofuRecipe(2.5)],
            [NoshBean(15), Water(125000)],
            [Tofu(2.5)],
            9000,
        ),
        (
            [TofuRecipe(1), SpicyTofuRecipe(1)],
            [NoshBean(6), Water(50000), PinchaPeppernut(1)],
            [SpicyTofu(1)],
            4000,
        ),
        (
            [TofuRecipe(1), NoshSprout(7)],
            [NoshBean(5), Water(50000)],
            [Tofu(1)],
            3600,
        ),
    ],
)
def test_compound(
    part_list: List[Processor],
    expected_consumption: List[Resource],
    expected_production: List[Resource],
    expected_calories: float,
):
    """Test compound"""
    compound = Compound(part_list)
    expected_consumption_bank = ResourceBank(*expected_consumption)
    expected_production_bank = ResourceBank(*expected_production)
    assert compound.consumption.resource_dict == expected_consumption_bank.resource_dict
    assert compound.production.resource_dict == expected_production_bank.resource_dict
    assert compound.calories == expected_calories


@pytest.mark.parametrize(
    "part_list, producer, expected_processor_list",
    [
        (
            [SpicyTofuRecipe(1)],
            TofuRecipe(),
            [SpicyTofuRecipe(1), TofuRecipe(1)],
        ),
        (
            [SpicyTofuRecipe(1.1)],
            TofuRecipe(),
            [SpicyTofuRecipe(1.1), TofuRecipe(1.1)],
        ),
    ],
)
def test_compound_producer(
    part_list: List[Processor],
    producer: Processor,
    expected_processor_list: List[Processor],
):
    """Test compound producer"""
    compound = Compound(part_list)
    compound.add_producer(producer)
    assert compound.processor_list == expected_processor_list


@pytest.mark.parametrize(
    "part_list, consumer, expected_processor_list",
    [
        (
            [TofuRecipe(1)],
            SpicyTofuRecipe(),
            [TofuRecipe(1), SpicyTofuRecipe(1)],
        ),
        (
            [TofuRecipe(1.1)],
            SpicyTofuRecipe(),
            [TofuRecipe(1.1), SpicyTofuRecipe(1.1)],
        ),
    ],
)
def test_compound_consumer(
    part_list: List[Processor],
    consumer: Processor,
    expected_processor_list: List[Processor],
):
    """Test compound producer"""
    compound = Compound(part_list)
    compound.add_consumer(consumer)
    assert compound.processor_list == expected_processor_list
