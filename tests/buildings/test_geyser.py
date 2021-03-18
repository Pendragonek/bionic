"""Test entity"""
from typing import Tuple

import pytest

from bionic.buildings.geyser import Geyser


@pytest.mark.parametrize(
    "geyser_params, current_time, expected",
    [
        ((4.0, 10, 20, 2.4, 4.6), 0, True),
        ((4.0, 10, 20, 2.4, 4.6), 10, False),
        ((4.0, 10, 20, 2.4, 4.6), 1500, False),
    ]
)
def test_geyser_is_erupting(geyser_params: Tuple[float, int, int, float, float], current_time: int, expected: bool):
    """Test geyser is erupting"""
    geyser = Geyser(*geyser_params)
    assert geyser.is_erupting(current_time) is expected


@pytest.mark.parametrize(
    "geyser_params, current_time, expected",
    [
        ((4.0, 10, 20, 2.4, 4.6), 100, True),
        ((4.0, 10, 20, 2.4, 4.6), 1500, False),
    ]
)
def test_geyser_is_active(geyser_params: Tuple[float, int, int, float, float], current_time: int, expected: bool):
    """Test geyser is active"""
    geyser = Geyser(*geyser_params)
    assert geyser.is_active(current_time) is expected
