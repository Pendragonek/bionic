"""Geyser class"""
from dataclasses import dataclass

from bionic.elements import Element, ElementBank

CYCLE_LENGTH = 600


@dataclass
class Geyser:
    """Geyser class"""

    output_element: Element
    eruption_time: int
    eruption_period: int
    activity_time: float
    activity_period: float

    def is_erupting(self, time: int) -> bool:
        """Return if geyser is erupting based on a given time"""
        if not self.is_active(time):
            return False
        return time % self.eruption_period < self.eruption_time

    def is_active(self, time: int) -> bool:
        """Return if geyser is active based on a given time"""
        return time % int(CYCLE_LENGTH * self.activity_period) < int(
            CYCLE_LENGTH * self.activity_time
        )

    def process(self, element_bank: ElementBank, time: int) -> None:
        """Process elements"""
        if self.is_erupting(time):
            element_bank.add(self.output_element)
