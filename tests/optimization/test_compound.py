"""Test compound"""

import json
from typing import List

import pytest

from bionic.optimization.compound import Compound
from bionic.processors import CalorieProcessor, Duplicant, Processor
from bionic.processors.plants import NoshSprout
from bionic.processors.recipes import SpicyTofuRecipe, TofuRecipe
from bionic.resources import Resource, ResourceBank
from bionic.resources.elements import Dirt, Ethanol, Water
from bionic.resources.food import NoshBean, PinchaPeppernut, SpicyTofu, Tofu

TEST_FILE_NAME = "test_file.json"


@pytest.mark.parametrize(
    "processor_list, expected_resource_balance, expected_calories",
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
    processor_list: List[Processor],
    expected_resource_balance: List[Resource],
    expected_calories: float,
):
    """Test compound"""
    compound = Compound(processor_list)
    expected_resource_balance_bank = ResourceBank(*expected_resource_balance)
    assert compound.resource_balance == expected_resource_balance_bank
    assert compound.calories == expected_calories


@pytest.mark.parametrize(
    "processor_list, producer, expected_processor_list",
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
def test_compound_add_resource_producer(
    processor_list: List[Processor],
    producer: Processor,
    expected_processor_list: List[Processor],
):
    """Test compound resource producer"""
    compound = Compound(processor_list)
    compound.add_resource_producer(producer)
    assert compound.processor_list == expected_processor_list


@pytest.mark.parametrize(
    "processor_list, consumer, expected_processor_list",
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
def test_compound_add_resource_consumer(
    processor_list: List[Processor],
    consumer: Processor,
    expected_processor_list: List[Processor],
):
    """Test compound resource consumer"""
    compound = Compound(processor_list)
    compound.add_resource_consumer(consumer)
    assert compound.processor_list == expected_processor_list


@pytest.mark.parametrize(
    "processor_list, calorie_processor, expected_processor_list",
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
def test_compound_add_calorie_producer(
    processor_list: List[Processor],
    calorie_processor: CalorieProcessor,
    expected_processor_list: List[Processor],
):
    """Test compound calorie producer"""
    compound = Compound(processor_list)
    compound.add_calorie_producer(calorie_processor)
    assert compound.processor_list == expected_processor_list


@pytest.mark.parametrize(
    "processor_list, calorie_processor, expected_processor_list",
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
def test_compound_add_calorie_consumer(
    processor_list: List[Processor],
    calorie_processor: CalorieProcessor,
    expected_processor_list: List[Processor],
):
    """Test compound calorie consumer"""
    compound = Compound(processor_list)
    compound.add_calorie_consumer(calorie_processor)
    assert compound.processor_list == expected_processor_list


@pytest.mark.parametrize(
    "processor_list, expected_data",
    [
        ([], []),
        (
            [TofuRecipe(amount=2)],
            [
                {
                    "location": {
                        "module": "bionic.processors.recipes.tofu_recipe",
                        "name": "TofuRecipe",
                    },
                    "params": {"amount": 2.0},
                },
            ],
        ),
        (
            [NoshSprout(amount=1, domesticated=True)],
            [
                {
                    "location": {
                        "module": "bionic.processors.plants.nosh_sprout",
                        "name": "NoshSprout",
                    },
                    "params": {"amount": 1.0, "domesticated": True},
                },
            ],
        ),
        (
            [TofuRecipe(amount=2), TofuRecipe(amount=1)],
            [
                {
                    "location": {
                        "module": "bionic.processors.recipes.tofu_recipe",
                        "name": "TofuRecipe",
                    },
                    "params": {"amount": 2.0},
                },
                {
                    "location": {
                        "module": "bionic.processors.recipes.tofu_recipe",
                        "name": "TofuRecipe",
                    },
                    "params": {"amount": 1.0},
                },
            ],
        ),
    ],
)
def test_compound_save_to_file(
    processor_list: List[Processor], expected_data: List[dict]
):
    """Test save to file"""
    compound = Compound(processor_list)
    compound.save_to_file(TEST_FILE_NAME)
    with open(TEST_FILE_NAME, encoding="utf-8") as file:
        data = json.load(file)
    assert data == expected_data


@pytest.mark.parametrize(
    "file_data, expected_processor_list",
    [
        ([], []),
        (
            [
                {
                    "location": {
                        "module": "bionic.processors.recipes.tofu_recipe",
                        "name": "TofuRecipe",
                    },
                    "params": {"amount": 2.0},
                },
            ],
            [TofuRecipe(amount=2)],
        ),
        (
            [
                {
                    "location": {
                        "module": "bionic.processors.plants.nosh_sprout",
                        "name": "NoshSprout",
                    },
                    "params": {"amount": 1.0, "domesticated": True},
                },
            ],
            [NoshSprout(amount=1, domesticated=True)],
        ),
        (
            [
                {
                    "location": {
                        "module": "bionic.processors.recipes.tofu_recipe",
                        "name": "TofuRecipe",
                    },
                    "params": {"amount": 2.0},
                },
                {
                    "location": {
                        "module": "bionic.processors.recipes.tofu_recipe",
                        "name": "TofuRecipe",
                    },
                    "params": {"amount": 1.0},
                },
            ],
            [TofuRecipe(amount=2), TofuRecipe(amount=1)],
        ),
    ],
)
def test_compound_from_file(
    file_data: List[dict], expected_processor_list: List[Processor]
):
    """Test save to file"""
    with open(TEST_FILE_NAME, mode="w", encoding="utf-8") as file:
        json.dump(file_data, file)
    compound = Compound.from_file(TEST_FILE_NAME)
    assert compound.processor_list == expected_processor_list
