"""Test entity"""
from typing import List, Tuple

import pytest

from bionic.dataclasses import Element
from bionic.dataclasses.entity import Entity, calculate_combined_entity_temperature

TEST_ELEMENT_NAME = "Test Element"


def test_entity_heat():
    """Test entity heat"""
    shc = 4.179
    mass = 1000
    temperature = 10
    element = Element(TEST_ELEMENT_NAME, shc)
    entity = Entity(element, mass, temperature)
    assert entity.heat == 41790


@pytest.mark.parametrize(
    "params_list, expected",
    [
        ([(2.400, 1000, 10)], 10),
        ([(2.400, 1000, 10), (2.400, 1000, 40)], 25),
        ([(2.400, 1000, 10), (2.400, 4000, 40)], 34),
        ([(2.400, 5000, 10), (1.000, 4000, 40)], 17.5),
    ]
)
def test_calculate_combined_entity_temperature(params_list: List[Tuple[float, float, float]], expected: float):
    """Test calculate combined entity temperature"""
    entity_list = list()
    for params in params_list:
        element = Element(TEST_ELEMENT_NAME, params[0])
        entity = Entity(element, params[1], params[2])
        entity_list.append(entity)
    combined_temperature = calculate_combined_entity_temperature(*entity_list)
    assert combined_temperature == expected
