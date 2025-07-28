"""Test food."""

from bionic.resources.food import Tofu


def test_food_calories() -> None:
    """Test food calories."""
    tofu = Tofu(amount=2)
    assert tofu.calories == 2 * 3600
