"""Resource bank"""

from typing import Dict, Type

from bionic.resources.resource import Resource


class ResourceBank:
    """Resource bank class"""

    def __init__(self, *args: Resource):
        self.resource_dict: Dict[Type[Resource], Resource] = {}
        for resource in args:
            self.add(resource)

    def get(self, resource_type: Type[Resource]) -> Resource:
        """Get resource based on resource type"""
        return self.resource_dict.get(resource_type) or resource_type()

    def add(self, resource: Resource):
        """Add resource to bank"""
        if not resource.amount:
            return
        element_type = type(resource)
        if element_type in self.resource_dict:
            self.resource_dict[element_type] += resource
        else:
            self.resource_dict[element_type] = resource

    def remove(self, resource: Resource):
        """Remove resource from bank"""
        resource_type = type(resource)
        stored_element = self.get(resource_type)
        if stored_element.amount < resource.amount:
            raise ArithmeticError
        if stored_element.amount == 0:
            return
        stored_element.amount -= resource.amount
        if not stored_element.amount:
            del self.resource_dict[resource_type]
