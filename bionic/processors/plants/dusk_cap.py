"""Dusk cap."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bionic.processors.plants.plant import Plant
from bionic.resources.elements import Slime
from bionic.resources.food import Mushroom

if TYPE_CHECKING:
    from bionic.resources import Resource


class DuskCap(Plant):
    """Dusk cap class."""

    @property
    def growth_speed(self) -> int:
        """Return growth of the plant."""
        return 30

    @property
    def irrigation(self) -> Resource | None:
        """Return irrigation per cycle of the plant."""
        return None

    @property
    def fertilizer(self) -> Resource:
        """Return fertilizer per cycle of the plant."""
        return Slime(amount=4000)

    @property
    def crop(self) -> Resource:
        """Return crop of the plant."""
        return Mushroom(amount=1)
