"""Geyser class."""

from bionic.processors import Processor
from bionic.resources import Resource, ResourceBank
from bionic.resources.elements import Element

CYCLE_LENGTH = 600


class Geyser(Processor):
    """Geyser class."""

    amount = 1.0
    output_element: Element
    eruption_time: int
    eruption_period: int
    activity_time: float
    activity_period: float

    @property
    def resource_consumption_per_unit(self) -> list[Resource]:
        """Resource consumption per unit property."""
        return []

    @property
    def resource_production_per_unit(self) -> list[Resource]:
        """Resource production per unit property."""
        return [
            self.output_element
            * CYCLE_LENGTH
            * self.eruption_time
            / self.eruption_period
            * self.activity_time
            / self.activity_period,
        ]

    def is_erupting(self, time: int) -> bool:
        """Return if geyser is erupting based on a given time."""
        if not self.is_active(time):
            return False
        return time % self.eruption_period < self.eruption_time

    def is_active(self, time: int) -> bool:
        """Return if geyser is active based on a given time."""
        return time % int(CYCLE_LENGTH * self.activity_period) < int(
            CYCLE_LENGTH * self.activity_time,
        )

    def process(self, element_bank: ResourceBank, time: int) -> None:
        """Process elements."""
        if self.is_erupting(time):
            element_bank.add(self.output_element)
