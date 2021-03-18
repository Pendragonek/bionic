"""Geyser class"""
from dataclasses import dataclass

from bionic.entities import Entity, EntityBank

CYCLE_LENGTH = 600


@dataclass
class Geyser:
    """Geyser class"""
    output_entity: Entity
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
        return time % int(CYCLE_LENGTH * self.activity_period) < int(CYCLE_LENGTH * self.activity_time)

    def process(self, entity_bank: EntityBank, time: int):
        """Process elements"""
        if self.is_erupting(time):
            entity_bank.add(self.output_entity)
