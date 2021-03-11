"""Test entity"""
from typing import List, Tuple

import pytest

from bionic.dataclasses import Entity
from bionic.dataclasses.entity import calculate_combined_entity_temperature
from bionic.elements import Element, WATER, HYDROGEN, IGNEOUS_ROCK

TEST_ELEMENT_NAME = "Test Element"


@pytest.mark.parametrize(
    "element, mass, temperature, expected_heat",
    [
        (WATER, 1000, 10, 41790),
        (HYDROGEN, 2000, 20, 96000),
    ]
)
def test_entity_heat(element: Element, mass: float, temperature: float, expected_heat: float):
    """Test entity heat"""
    entity = Entity(element, mass, temperature)
    assert entity.heat == expected_heat


@pytest.mark.parametrize(
    "params_list, expected",
    [
        ([(HYDROGEN, 1000, 10)], 10),
        ([(HYDROGEN, 1000, 10), (HYDROGEN, 1000, 40)], 25),
        ([(HYDROGEN, 1000, 10), (HYDROGEN, 4000, 40)], 34),
        ([(HYDROGEN, 5000, 10), (IGNEOUS_ROCK, 4000, 40)], 17.5),
    ]
)
def test_calculate_combined_entity_temperature(params_list: List[Tuple[Element, float, float]], expected: float):
    """Test calculate combined entity temperature"""
    entity_list = list()
    for params in params_list:
        entity = Entity(*params)
        entity_list.append(entity)
    combined_temperature = calculate_combined_entity_temperature(*entity_list)
    assert combined_temperature == expected
