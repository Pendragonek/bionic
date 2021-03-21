"""Test element"""
from typing import List

import pytest

from bionic.buildings import Geyser
from bionic.elements import Element, ElementBank, Steam

TEST_GEYSER_OUTPUT_ELEMENT = Steam(1000, 110)
TEST_GEYSER = Geyser(TEST_GEYSER_OUTPUT_ELEMENT, 10, 20, 2.4, 4.6)


@pytest.mark.parametrize(
    "current_time, expected",
    [
        (0, True),
        (10, False),
        (1500, False),
    ]
)
def test_geyser_is_erupting(current_time: int, expected: bool):
    """Test geyser is erupting"""
    assert TEST_GEYSER.is_erupting(current_time) is expected


@pytest.mark.parametrize(
    "current_time, expected",
    [
        (100, True),
        (1500, False),
    ]
)
def test_geyser_is_active(current_time: int, expected: bool):
    """Test geyser is active"""
    assert TEST_GEYSER.is_active(current_time) is expected


@pytest.mark.parametrize(
    "current_time, initial_state, expected_state",
    [
        (0, [], [TEST_GEYSER_OUTPUT_ELEMENT]),
        (10, [], []),
    ]
)
def test_geyser_process(current_time: int, initial_state: List[Element], expected_state: List[Element]):
    """Test geyser is erupting"""
    element_bank = ElementBank(*initial_state)
    TEST_GEYSER.process(element_bank, current_time)
    assert element_bank.element_dict == ElementBank(*expected_state).element_dict
