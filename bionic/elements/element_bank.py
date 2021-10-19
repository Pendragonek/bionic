"""Element bank"""

from typing import Dict, Type

from bionic.elements.element import Element


class ElementBank:
    """Element bank class"""

    def __init__(self, *args: Element):
        self.element_dict: Dict[Type[Element], Element] = {}
        for element in args:
            self.add(element)

    def get(self, element_type: Type[Element]) -> Element:
        """Get element based on element type"""
        return self.element_dict.get(element_type) or element_type()

    def add(self, element: Element):
        """Add element to bank"""
        element_type = type(element)
        if element_type in self.element_dict:
            self.element_dict[element_type] += element
        else:
            self.element_dict[element_type] = element

    def remove(self, element: Element):
        """Remove element from bank"""
        stored_element = self.get(type(element))
        if stored_element.amount < element.amount:
            raise ArithmeticError
        if stored_element.amount == 0:
            return
        stored_element.amount -= element.amount

    @staticmethod
    def calculate_combined_element_temperature(*element_list: Element) -> float:
        """Calculate combined temperature of two entities"""
        total_heat = 0.0
        total_heat_capacity = 0.0
        for element in element_list:
            total_heat += element.heat
            total_heat_capacity += element.shc * element.amount
        return total_heat / total_heat_capacity
