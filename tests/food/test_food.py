"""Test food"""

from bionic.food.tofu import Tofu


def test_food_calories():
    """Test food calories"""
    tofu = Tofu(2)
    assert tofu.calories == 2 * 3600
