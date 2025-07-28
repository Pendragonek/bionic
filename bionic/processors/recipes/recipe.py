"""Recipe."""

from abc import abstractmethod

from bionic.processors import CalorieProcessor
from bionic.resources import Resource
from bionic.resources.food import Food


class Recipe(CalorieProcessor):
    """Recipe class."""

    @property
    @abstractmethod
    def ingredient_list(self) -> list[Resource]:
        """Ingredient list property."""

    @property
    @abstractmethod
    def product(self) -> Food:
        """Product property."""

    @property
    def resource_consumption_per_unit(self) -> list[Resource]:
        """Resource consumption per unit property."""
        return self.ingredient_list

    @property
    def resource_production_per_unit(self) -> list[Resource]:
        """Resource production per unit property."""
        return [self.product]
