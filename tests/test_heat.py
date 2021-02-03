"""Test heat calculations"""
from bionic.heat import calculate_heat_amount


def test_calculate_heat_amount():
    shc = 4.179
    mass = 1000
    temperature = 10
    heat_amount = calculate_heat_amount(shc, mass, temperature)
    assert heat_amount == 41790
