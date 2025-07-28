"""Test element."""

import pytest

from bionic.processors.buildings import Geyser
from bionic.resources import ResourceBank
from bionic.resources.elements import Element, Steam

TEST_GEYSER_OUTPUT_ELEMENT = Steam(amount=1000, temperature=110)
TEST_GEYSER = Geyser(
    output_element=TEST_GEYSER_OUTPUT_ELEMENT,
    eruption_time=10,
    eruption_period=20,
    activity_time=2.4,
    activity_period=4.6,
)


@pytest.mark.parametrize(
    ("current_time", "expected"),
    [
        (0, True),
        (10, False),
        (1500, False),
    ],
)
def test_geyser_is_erupting(current_time: int, expected: bool) -> None:
    """Test geyser is erupting."""
    assert TEST_GEYSER.is_erupting(current_time) is expected


@pytest.mark.parametrize(
    ("current_time", "expected"),
    [
        (100, True),
        (1500, False),
    ],
)
def test_geyser_is_active(current_time: int, expected: bool) -> None:
    """Test geyser is active."""
    assert TEST_GEYSER.is_active(current_time) is expected


@pytest.mark.parametrize(
    ("current_time", "initial_state", "expected_state"),
    [
        (0, [], [TEST_GEYSER_OUTPUT_ELEMENT]),
        (10, [], []),
    ],
)
def test_geyser_process(
    current_time: int,
    initial_state: list[Element],
    expected_state: list[Element],
) -> None:
    """Test geyser is erupting."""
    element_bank = ResourceBank(*initial_state)
    TEST_GEYSER.process(element_bank, current_time)
    assert element_bank.resource_dict == ResourceBank(*expected_state).resource_dict
