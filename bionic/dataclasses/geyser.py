"""Geyser class"""
from dataclasses import dataclass

CYCLE_LENGTH = 600


@dataclass
class Geyser:
    """Geyser class"""
    mass_output: float
    eruption_time: int
    eruption_period: int
    activity_time: float
    activity_period: float

    def is_erupting(self, time: int) -> bool:
        """Return if geyser is erupting based on a given time"""
        return time % self.eruption_period < self.eruption_time

    def is_active(self, time: int) -> bool:
        """Return if geyser is active based on a given time"""
        return time % int(CYCLE_LENGTH * self.activity_period) < int(CYCLE_LENGTH * self.activity_time)
