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
        resource_type = type(resource)
        if resource_type in self.resource_dict:
            self.resource_dict[resource_type] += resource
        else:
            self.resource_dict[resource_type] = resource
        if not self.resource_dict[resource_type].amount:
            del self.resource_dict[resource_type]

    def subtract(self, resource: Resource):
        """Subtract resource from bank"""
        if not resource.amount:
            return
        resource_type = type(resource)
        if resource_type in self.resource_dict:
            self.resource_dict[resource_type] -= resource
        else:
            self.resource_dict[resource_type] = -resource
        if not self.resource_dict[resource_type].amount:
            del self.resource_dict[resource_type]
