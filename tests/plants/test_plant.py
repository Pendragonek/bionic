"""Test nosh sprout"""
from bionic.elements.dirt import Dirt
from bionic.elements.ethanol import Ethanol
from bionic.plants.nosh_sprout import NoshSprout
from bionic.resources.nosh_bean import NoshBean


def test_wild_plant():
    """Test wild plant"""
    nosh_sprout = NoshSprout()
    assert nosh_sprout.production_per_cycle == NoshBean(12 / 84)
    assert nosh_sprout.consumption_per_cycle == []


def test_domesticated_plant():
    """Test domesticated plant"""
    nosh_sprout = NoshSprout(domesticated=True)
    assert nosh_sprout.production_per_cycle == NoshBean(12 / 84 * 4)
    assert nosh_sprout.consumption_per_cycle == [Ethanol(20000), Dirt(5000)]
