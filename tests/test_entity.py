"""Test entity"""
from bionic.dataclasses import Element
from bionic.dataclasses.entity import Entity


def test_heat():
    name = "Water"
    shc = 4.179
    mass = 1000
    temperature = 10
    element = Element(name, shc)
    entity = Entity(element, mass, temperature)
    assert entity.heat == 41790
