"""Recipe"""

from abc import abstractmethod
from typing import List

from bionic.food.food import Food
from bionic.processors.calorie_processor import CalorieProcessor
from bionic.resources.resource import Resource


class Recipe(CalorieProcessor):
    """Recipe class"""

    @property
    @abstractmethod
    def ingredient_list(self) -> List[Resource]:
        """Ingredient list property"""

    @property
    @abstractmethod
    def product(self) -> Food:
        """Product property"""

    @property
    def consumption_per_unit(self) -> List[Resource]:
        """Consumption per unit property"""
        return self.ingredient_list

    @property
    def production_per_unit(self) -> List[Resource]:
        """Production per unit property"""
        return [self.product]

    @property
    def calories_per_unit(self) -> float:
        """Calories property"""
        calories = 0.0
        for ingredient in self.ingredient_list:
            if isinstance(ingredient, Food):
                calories -= ingredient.calories_per_unit
        calories += self.product.calories_per_unit
        return calories
