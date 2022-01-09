"""Test compound"""

from typing import List

import pytest

from bionic.buildings.compost import Compost
from bionic.buildings.ethanol_distiller import EthanolDistiller
from bionic.compound import Compound
from bionic.critters.pip import Pip
from bionic.elements.dirt import Dirt
from bionic.elements.ethanol import Ethanol
from bionic.elements.water import Water
from bionic.food.nosh_bean import NoshBean
from bionic.food.pincha_peppernut import PinchaPeppernut
from bionic.food.spicy_tofu import SpicyTofu
from bionic.food.tofu import Tofu
from bionic.plants.arbor_tree import ArborTree
from bionic.plants.bristle_blossom import BristleBlossom
from bionic.plants.nosh_sprout import NoshSprout
from bionic.plants.pincha_pepper import PinchaPepper
from bionic.processors.calorie_processor import CalorieProcessor
from bionic.processors.duplicant import Duplicant
from bionic.processors.processor import Processor
from bionic.recipes.gristle_berry_recipe import GristleBerryRecipe
from bionic.recipes.spicy_tofu_recipe import SpicyTofuRecipe
from bionic.recipes.stuffed_berry_recipe import StuffedBerryRecipe
from bionic.recipes.tofu_recipe import TofuRecipe
from bionic.resources.resource import Resource
from bionic.resources.resource_bank import ResourceBank


@pytest.mark.parametrize(
    "part_list, expected_resource_balance, expected_calories",
    [
        (
            [TofuRecipe(amount=4)],
            [NoshBean(amount=-24), Water(amount=-200000), Tofu(amount=4)],
            14400,
        ),
        (
            [TofuRecipe(amount=2.5)],
            [NoshBean(amount=-15), Water(amount=-125000), Tofu(amount=2.5)],
            9000,
        ),
        (
            [TofuRecipe(amount=1), SpicyTofuRecipe(amount=1)],
            [
                NoshBean(amount=-6),
                Water(amount=-50000),
                PinchaPeppernut(amount=-1),
                SpicyTofu(amount=1),
            ],
            4000,
        ),
        (
            [TofuRecipe(amount=1), NoshSprout(amount=7)],
            [NoshBean(amount=-5), Water(amount=-50000), Tofu(amount=1)],
            3600,
        ),
        (
            [TofuRecipe(amount=1), NoshSprout(amount=7, domesticated=True)],
            [
                NoshBean(amount=-2),
                Water(amount=-50000),
                Ethanol(amount=-140000),
                Dirt(amount=-35000),
                Tofu(amount=1),
            ],
            3600,
        ),
    ],
)
def test_compound_balance(
    part_list: List[Processor],
    expected_resource_balance: List[Resource],
    expected_calories: float,
):
    """Test compound"""
    compound = Compound(part_list)
    expected_resource_balance_bank = ResourceBank(*expected_resource_balance)
    assert compound.resource_balance == expected_resource_balance_bank
    assert compound.calories == expected_calories


@pytest.mark.parametrize(
    "part_list, producer, expected_processor_list",
    [
        (
            [SpicyTofuRecipe(amount=1)],
            TofuRecipe(),
            [SpicyTofuRecipe(amount=1), TofuRecipe(amount=1)],
        ),
        (
            [SpicyTofuRecipe(amount=1.1)],
            TofuRecipe(),
            [SpicyTofuRecipe(amount=1.1), TofuRecipe(amount=1.1)],
        ),
        (
            [TofuRecipe(amount=1)],
            NoshSprout(),
            [TofuRecipe(amount=1), NoshSprout(amount=42)],
        ),
        (
            [TofuRecipe(amount=1)],
            NoshSprout(domesticated=True),
            [TofuRecipe(amount=1), NoshSprout(amount=10.5, domesticated=True)],
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
            [TofuRecipe(amount=1)],
            SpicyTofuRecipe(),
            [TofuRecipe(amount=1), SpicyTofuRecipe(amount=1)],
        ),
        (
            [TofuRecipe(amount=1.1)],
            SpicyTofuRecipe(),
            [TofuRecipe(amount=1.1), SpicyTofuRecipe(amount=1.1)],
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
            [Duplicant(amount=9)],
            TofuRecipe(),
            [Duplicant(amount=9), TofuRecipe(amount=2.5)],
        ),
        (
            [Duplicant(amount=8)],
            SpicyTofuRecipe(amount=2),
            [Duplicant(amount=8), SpicyTofuRecipe(amount=2)],
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
            [TofuRecipe(amount=4)],
            SpicyTofuRecipe(),
            [TofuRecipe(amount=4), SpicyTofuRecipe(amount=4)],
        ),
        (
            [TofuRecipe(amount=3), SpicyTofuRecipe(amount=3)],
            Duplicant(),
            [TofuRecipe(amount=3), SpicyTofuRecipe(amount=3), Duplicant(amount=12)],
        ),
    ],
)
def test_compound_calorie_consumer(
    part_list: List[Processor],
    calorie_processor: CalorieProcessor,
    expected_processor_list: List[Processor],
):
    """Test compound calorie consumer"""
    compound = Compound(part_list)
    compound.add_calorie_consumer(calorie_processor)
    assert compound.processor_list == expected_processor_list


def test_stuff():
    """Test stuff"""
    compound = Compound([ArborTree(amount=12)])
    compound.add_processor(Pip(amount=12))
    compound.add_resource_consumer(EthanolDistiller())
    compound.add_resource_consumer(Compost())
    compound.add_resource_consumer(NoshSprout(domesticated=True))
    compound.add_resource_consumer(TofuRecipe())
    compound.add_resource_consumer(SpicyTofuRecipe())
    compound.add_processor(Duplicant(amount=12))
    compound.add_calorie_producer(StuffedBerryRecipe())
    compound.add_resource_producer(PinchaPepper())
    compound.add_resource_producer(GristleBerryRecipe())
    compound.add_resource_producer(BristleBlossom(domesticated=True))
    print(compound.processor_list)
    print(compound.resource_balance.resource_dict)
    print(compound.calories)
    assert False
