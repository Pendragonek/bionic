"""Test entity"""
from bionic.dataclasses import Element
from bionic.dataclasses.entity import Entity, calculate_combined_entity_temperature

TEST_ELEMENT_NAME = "Test Element"


def test_heat():
    shc = 4.179
    mass = 1000
    temperature = 10
    element = Element(TEST_ELEMENT_NAME, shc)
    entity = Entity(element, mass, temperature)
    assert entity.heat == 41790


def test_calculate_combined_entity_temperature():
    shc1 = 2.400
    mass1 = 5000
    temperature1 = 10
    element1 = Element(TEST_ELEMENT_NAME, shc1)
    entity1 = Entity(element1, mass1, temperature1)
    shc2 = 1.000
    mass2 = 4000
    temperature2 = 40
    element2 = Element(TEST_ELEMENT_NAME, shc2)
    entity2 = Entity(element2, mass2, temperature2)
    combined_temperature = calculate_combined_entity_temperature(entity1, entity2)
    assert combined_temperature == 17.5
