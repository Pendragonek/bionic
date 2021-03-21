"""Element bank"""
from typing import Dict, Type

from bionic.elements import Element
from bionic.elements.element import calculate_combined_element_temperature


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
        if type(element) in self.element_dict:
            stored_element = self.element_dict[type(element)]
            stored_element.temperature = calculate_combined_element_temperature(stored_element, element)
            stored_element.mass += element.mass
        else:
            self.element_dict[type(element)] = element

    def remove(self, element: Element):
        """Remove element from bank"""
        stored_element = self.get(type(element))
        if stored_element.mass < element.mass:
            raise ArithmeticError
        if stored_element.mass == 0:
            return
        stored_element.mass -= element.mass
