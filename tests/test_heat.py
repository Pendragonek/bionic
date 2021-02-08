"""Test heat calculations"""
from bionic.heat import calculate_heat_amount, calculate_temperature_delta


def test_calculate_heat_amount():
    shc = 4.179
    mass = 1000
    temperature = 10
    heat_amount = calculate_heat_amount(shc, mass, temperature)
    assert heat_amount == 41790


def test_calculate_temperature_delta():
    shc = 2.400
    mass = 1000
    heat_amount = 6000
    temperature_delta = calculate_temperature_delta(shc, mass, heat_amount)
    assert temperature_delta == 2.5
