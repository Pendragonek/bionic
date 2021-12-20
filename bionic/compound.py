"""Compound"""

from typing import List, Type

from bionic.processors.calorie_processor import CalorieProcessor
from bionic.processors.duplicant import Duplicant
from bionic.processors.processor import Processor
from bionic.recipes.recipe import Recipe
from bionic.resources.resource import Resource
from bionic.resources.resource_bank import ResourceBank


class Compound:
    """Compound class"""

    def __init__(self, processor_list: List[Processor]):
        self.consumption = ResourceBank()
        self.production = ResourceBank()
        self.calories: float = 0.0
        self.processor_list: List[Processor] = []
        for processor in processor_list:
            self.add_processor(processor)

    def add_processor(self, processor: Processor):
        """Add processor"""
        self.processor_list.append(processor)
        for consumed_resource in processor.consumption:
            consumed_resource_type = type(consumed_resource)
            produced_resource = self.production.get(consumed_resource_type)
            amount_diff = consumed_resource.amount - produced_resource.amount
            if amount_diff > 0:
                self.production.remove(produced_resource)
                self.consumption.add(consumed_resource_type(amount_diff))
            else:
                self.production.remove(consumed_resource)
        for produced_resource in processor.production:
            produced_resource_type: Type[Resource] = type(produced_resource)
            consumed_resource = self.consumption.get(produced_resource_type)
            amount_diff = produced_resource.amount - consumed_resource.amount
            if amount_diff > 0:
                self.consumption.remove(consumed_resource)
                self.production.add(produced_resource_type(amount_diff))
            else:
                self.consumption.remove(produced_resource)
        if isinstance(processor, (Duplicant, Recipe)):
            self.calories += processor.calories

    def add_producer(self, processor: Processor):
        """Add producer"""
        processor.amount = 1
        for product in processor.production:
            demand = self.consumption.get(type(product))
            if demand.amount == 0:
                continue
            processor.amount = demand.amount / product.amount
            self.add_processor(processor)

    def add_consumer(self, processor: Processor):
        """Add consumer"""
        processor.amount = 1
        for product in processor.consumption:
            supply = self.production.get(type(product))
            if supply.amount == 0:
                continue
            processor.amount = supply.amount / product.amount
            self.add_processor(processor)

    def add_calorie_processor(self, calorie_processor: CalorieProcessor):
        """Add calorie processor"""
        calorie_processor.amount = -self.calories / calorie_processor.calories_per_unit
        if calorie_processor.amount < 0:
            return
        self.add_processor(calorie_processor)
