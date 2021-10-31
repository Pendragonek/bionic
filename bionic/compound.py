"""Compound"""

from typing import List, Type

from bionic.processors.processor import Processor
from bionic.resources.resource import Resource
from bionic.resources.resource_bank import ResourceBank


class Compound:
    """Compound class"""

    def __init__(self, processor_list: List[Processor]):
        self.consumption = ResourceBank()
        self.production = ResourceBank()
        self.processor_list: List[Processor] = list()
        for processor in processor_list:
            self.add_processor(processor)

    def add_processor(self, processor: Processor):
        """Add processor"""
        self.processor_list.append(processor)
        for consumed_resource in processor.consumption:
            resource_type: Type[Resource] = type(consumed_resource)
            produced_resource = self.production.get(resource_type)
            amount_diff = consumed_resource.amount - produced_resource.amount
            if amount_diff > 0:
                self.production.remove(produced_resource)
                self.consumption.add(resource_type(amount_diff))
            else:
                self.production.remove(consumed_resource)
        for produced_resource in processor.production:
            resource_type: Type[Resource] = type(produced_resource)
            consumed_resource = self.consumption.get(resource_type)
            amount_diff = produced_resource.amount - consumed_resource.amount
            if amount_diff > 0:
                self.consumption.remove(consumed_resource)
                self.production.add(resource_type(amount_diff))
            else:
                self.consumption.remove(produced_resource)
