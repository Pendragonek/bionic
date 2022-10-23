"""Natural gas generator"""

from typing import List

from bionic.processors import Processor
from bionic.resources import Resource
from bionic.resources.elements import CarbonDioxide, NaturalGas, PollutedWater


class NaturalGasGenerator(Processor):
    """Natural gas generator class"""

    @property
    def resource_consumption_per_unit(self) -> List[Resource]:
        """Resource consumption per unit property"""
        return [NaturalGas(amount=54000)]

    @property
    def resource_production_per_unit(self) -> List[Resource]:
        """Resource production per unit property"""
        return [
            PollutedWater(amount=40500),
            CarbonDioxide(amount=13500),
        ]
