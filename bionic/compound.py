"""Compound"""

from typing import List, Type

from bionic.processors.calorie_processor import CalorieProcessor
from bionic.processors.processor import Processor
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
        for consumed_resource in processor.resource_consumption:
            consumed_resource_type = type(consumed_resource)
            produced_resource = self.production.get(consumed_resource_type)
            amount_diff = consumed_resource.amount - produced_resource.amount
            if amount_diff > 0:
                self.production.remove(produced_resource)
                self.consumption.add(consumed_resource_type(amount_diff))
            else:
                self.production.remove(consumed_resource)
        for produced_resource in processor.resource_production:
            produced_resource_type: Type[Resource] = type(produced_resource)
            consumed_resource = self.consumption.get(produced_resource_type)
            amount_diff = produced_resource.amount - consumed_resource.amount
            if amount_diff > 0:
                self.consumption.remove(consumed_resource)
                self.production.add(produced_resource_type(amount_diff))
            else:
                self.consumption.remove(produced_resource)
        print(type(processor))
        if isinstance(processor, CalorieProcessor):
            print(self.calories)
            self.calories -= processor.calorie_consumption
            print(self.calories)
            self.calories += processor.calorie_production
            print(self.calories)

    def add_resource_producer(self, processor: Processor):
        """Add resource producer"""
        processor.amount = 1
        for product in processor.resource_production:
            demand = self.consumption.get(type(product))
            if demand.amount == 0:
                continue
            processor.amount = demand.amount / product.amount
            self.add_processor(processor)

    def add_resource_consumer(self, processor: Processor):
        """Add resource consumer"""
        processor.amount = 1
        for product in processor.resource_consumption:
            supply = self.production.get(type(product))
            if supply.amount == 0:
                continue
            processor.amount = supply.amount / product.amount
            self.add_processor(processor)

    def add_calorie_producer(self, calorie_processor: CalorieProcessor):
        """Add calorie producer"""
        if self.calories >= 0 or calorie_processor.calorie_production_per_unit == 0:
            return
        calorie_processor.amount = (
            -self.calories / calorie_processor.calorie_production_per_unit
        )
        self.add_processor(calorie_processor)

    def add_calorie_consumer(self, calorie_processor: CalorieProcessor):
        """Add calorie consumer"""
        if self.calories <= 0 or calorie_processor.calorie_consumption_per_unit == 0:
            return
        calorie_processor.amount = (
            self.calories / calorie_processor.calorie_consumption_per_unit
        )
        self.add_processor(calorie_processor)
