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
    def resource_consumption_per_unit(self) -> List[Resource]:
        """Resource consumption per unit property"""
        return self.ingredient_list

    @property
    def resource_production_per_unit(self) -> List[Resource]:
        """Resource production per unit property"""
        return [self.product]

    @property
    def calorie_consumption_per_unit(self) -> float:
        """Calorie consumption per unit property"""
        calories = 0.0
        for ingredient in self.ingredient_list:
            if isinstance(ingredient, Food):
                calories += ingredient.calories_per_unit
        return calories

    @property
    def calorie_production_per_unit(self) -> float:
        """Calorie production per unit property"""
        return self.product.calories_per_unit
