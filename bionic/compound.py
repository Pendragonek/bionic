"""Compound"""

import json
from typing import List

from bionic.processors.calorie_processor import CalorieProcessor
from bionic.processors.processor import Processor
from bionic.resources.resource_bank import ResourceBank


class Compound:
    """Compound class"""

    def __init__(self, processor_list: List[Processor]):
        self.resource_balance = ResourceBank()
        self.calories: float = 0.0
        self.processor_list: List[Processor] = []
        for processor in processor_list:
            self.add_processor(processor)

    def add_processor(self, processor: Processor):
        """Add processor"""
        self.processor_list.append(processor)
        for consumed_resource in processor.resource_consumption:
            self.resource_balance.subtract(consumed_resource)
        for produced_resource in processor.resource_production:
            self.resource_balance.add(produced_resource)
        if isinstance(processor, CalorieProcessor):
            self.calories -= processor.calorie_consumption
            self.calories += processor.calorie_production

    def add_resource_producer(self, processor: Processor):
        """Add resource producer"""
        for product in processor.resource_production_per_unit:
            demand = self.resource_balance.get(type(product))
            if demand.amount >= 0:
                continue
            processor.amount = -demand.amount / product.amount
            self.add_processor(processor)
            break

    def add_resource_consumer(self, processor: Processor):
        """Add resource consumer"""
        for product in processor.resource_consumption_per_unit:
            supply = self.resource_balance.get(type(product))
            if supply.amount <= 0:
                continue
            processor.amount = supply.amount / product.amount
            self.add_processor(processor)
            break

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

    def save_to_file(self, file_name: str):
        """Save current state to file"""
        saved_data = []
        for processor in self.processor_list:
            processor_name = type(processor).__name__
            processor_dict = processor.dict()
            processor_dict["name"] = processor_name
            saved_data.append(processor_dict)
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(saved_data, file)
