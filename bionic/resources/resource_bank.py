"""Resource bank."""

from bionic.resources.resource import Resource


class ResourceBank:
    """Resource bank class."""

    def __init__(self, *args: Resource) -> None:
        self.resource_dict: dict[type[Resource], Resource] = {}
        for resource in args:
            self.add(resource)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ResourceBank):
            return False
        return self.resource_dict == other.resource_dict

    def get(self, resource_type: type[Resource]) -> Resource:
        """Get resource based on resource type."""
        return self.resource_dict.get(resource_type) or resource_type()

    def add(self, resource: Resource) -> None:
        """Add resource to bank."""
        if not resource.amount:
            return
        resource_type = type(resource)
        if resource_type in self.resource_dict:
            self.resource_dict[resource_type] += resource
        else:
            self.resource_dict[resource_type] = resource
        if not self.resource_dict[resource_type].amount:
            del self.resource_dict[resource_type]

    def subtract(self, resource: Resource) -> None:
        """Subtract resource from bank."""
        if not resource.amount:
            return
        resource_type = type(resource)
        if resource_type in self.resource_dict:
            self.resource_dict[resource_type] -= resource
        else:
            self.resource_dict[resource_type] = -resource
        if not self.resource_dict[resource_type].amount:
            del self.resource_dict[resource_type]
