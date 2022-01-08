"""Element"""

from abc import abstractmethod

from bionic.resources.resource import Resource


class Element(Resource):
    """Element class"""

    temperature: float = 0

    @property
    @abstractmethod
    def shc(self) -> float:
        """Return SHC of the element"""

    @property
    def heat(self) -> float:
        """Return heat amount"""
        return self.shc * self.amount * self.temperature

    def temperature_add(self, other: "Element") -> "Element":
        """Temperature add"""
        element_type = type(self)
        if not isinstance(other, element_type):
            raise TypeError
        mass = self.amount + other.amount
        temperature = (
            self.amount * self.temperature + other.amount * other.temperature
        ) / mass
        return element_type(amount=mass, temperature=temperature)


def calculate_combined_element_temperature(*element_list: Element) -> float:
    """Calculate combined temperature of two entities"""
    total_heat = 0.0
    total_heat_capacity = 0.0
    for element in element_list:
        total_heat += element.heat
        total_heat_capacity += element.shc * element.amount
    return total_heat / total_heat_capacity
