"""Test heat calculations"""
from bionic.heat import calculate_heat_amount, calculate_temperature_delta, calculate_combined_temperature


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


def test_calculate_combined_temperature():
    shc1 = 2.400
    mass1 = 1000
    temperature1 = 10
    shc2 = 2.400
    mass2 = 1000
    temperature2 = 40
    combined_temperature = calculate_combined_temperature(shc1, mass1, temperature1, shc2, mass2, temperature2)
    assert combined_temperature == 25


def test_calculate_combined_temperature_different_mass():
    shc1 = 2.400
    mass1 = 1000
    temperature1 = 10
    shc2 = 2.400
    mass2 = 4000
    temperature2 = 40
    combined_temperature = calculate_combined_temperature(shc1, mass1, temperature1, shc2, mass2, temperature2)
    assert combined_temperature == 34


def test_calculate_combined_temperature_different_mass_and_shc():
    shc1 = 2.400
    mass1 = 5000
    temperature1 = 10
    shc2 = 1.000
    mass2 = 4000
    temperature2 = 40
    combined_temperature = calculate_combined_temperature(shc1, mass1, temperature1, shc2, mass2, temperature2)
    assert combined_temperature == 17.5
