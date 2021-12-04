"""Recipe"""

from abc import abstractmethod
from typing import List

from bionic.food.food import Food
from bionic.processors.processor import Processor
from bionic.resources.resource import Resource


class Recipe(Processor):
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
    def consumption(self) -> List[Resource]:
        """Consumption property"""
        ingredient_list = list()
        for ingredient in self.ingredient_list:
            ingredient_list.append(ingredient * self.amount)
        return ingredient_list

    @property
    def production(self) -> List[Resource]:
        """Production property"""
        return [self.product * self.amount]

    @property
    def calories(self) -> float:
        """Calories property"""
        calories = 0
        for ingredient in self.ingredient_list:
            if isinstance(ingredient, Food):
                calories -= ingredient.calories
        calories += self.product.calories
        return calories * self.amount
