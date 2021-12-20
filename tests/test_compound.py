"""Test compound"""

from typing import List

import pytest

from bionic.compound import Compound
from bionic.elements.dirt import Dirt
from bionic.elements.ethanol import Ethanol
from bionic.elements.water import Water
from bionic.food.nosh_bean import NoshBean
from bionic.food.pincha_peppernut import PinchaPeppernut
from bionic.food.spicy_tofu import SpicyTofu
from bionic.food.tofu import Tofu
from bionic.plants.nosh_sprout import NoshSprout
from bionic.processors.calorie_processor import CalorieProcessor
from bionic.processors.duplicant import Duplicant
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
        (
            [TofuRecipe(1), NoshSprout(7, domesticated=True)],
            [NoshBean(2), Water(50000), Ethanol(140000), Dirt(35000)],
            [Tofu(1)],
            3600,
        ),
    ],
)
def test_compound_balance(
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
        (
            [TofuRecipe(1)],
            NoshSprout(),
            [TofuRecipe(1), NoshSprout(42)],
        ),
        (
            [TofuRecipe(1)],
            NoshSprout(domesticated=True),
            [TofuRecipe(1), NoshSprout(10.5, domesticated=True)],
        ),
    ],
)
def test_compound_resource_producer(
    part_list: List[Processor],
    producer: Processor,
    expected_processor_list: List[Processor],
):
    """Test compound resource producer"""
    compound = Compound(part_list)
    compound.add_resource_producer(producer)
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
def test_compound_resource_consumer(
    part_list: List[Processor],
    consumer: Processor,
    expected_processor_list: List[Processor],
):
    """Test compound resource consumer"""
    compound = Compound(part_list)
    compound.add_resource_consumer(consumer)
    assert compound.processor_list == expected_processor_list


@pytest.mark.parametrize(
    "part_list, calorie_processor, expected_processor_list",
    [
        (
            [Duplicant(9)],
            TofuRecipe(),
            [Duplicant(9), TofuRecipe(2.5)],
        ),
        (
            [Duplicant(8)],
            SpicyTofuRecipe(2),
            [Duplicant(8), SpicyTofuRecipe(2)],
        ),
    ],
)
def test_compound_calorie_producer(
    part_list: List[Processor],
    calorie_processor: CalorieProcessor,
    expected_processor_list: List[Processor],
):
    """Test compound calorie producer"""
    compound = Compound(part_list)
    compound.add_calorie_producer(calorie_processor)
    assert compound.processor_list == expected_processor_list


@pytest.mark.parametrize(
    "part_list, calorie_processor, expected_processor_list",
    [
        (
            [TofuRecipe(4)],
            SpicyTofuRecipe(),
            [TofuRecipe(4), SpicyTofuRecipe(4)],
        ),
        (
            [TofuRecipe(3), SpicyTofuRecipe(3)],
            Duplicant(),
            [TofuRecipe(3), SpicyTofuRecipe(3), Duplicant(12)],
        ),
    ],
)
def test_compound_calorie_consumer(
    part_list: List[Processor],
    calorie_processor: CalorieProcessor,
    expected_processor_list: List[Processor],
):
    """Test compound calorie producer"""
    compound = Compound(part_list)
    compound.add_calorie_consumer(calorie_processor)
    assert compound.processor_list == expected_processor_list
