"""Test heat calculations"""
import pytest

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


@pytest.mark.parametrize(
    "shc1, mass1, temperature1, shc2, mass2, temperature2, expected",
    [
        (2.400, 1000, 10, 2.400, 1000, 40, 25),
        (2.400, 1000, 10, 2.400, 4000, 40, 34),
        (2.400, 5000, 10, 1.000, 4000, 40, 17.5),
    ]
)
def test_calculate_combined_temperature(shc1, mass1, temperature1, shc2, mass2, temperature2, expected):
    combined_temperature = calculate_combined_temperature(shc1, mass1, temperature1, shc2, mass2, temperature2)
    assert combined_temperature == expected
