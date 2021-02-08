"""Heat calculations"""


def calculate_heat_amount(shc: float, mass: float, temperature: float) -> float:
    """Calculate heat amount based on SHC, mass and temperature"""
    return shc * mass * temperature


def calculate_temperature_delta(shc: float, mass: float, heat_amount: float) -> float:
    """Calculate temperature delta based on SHC, mass and heat transferred"""
    return heat_amount / (shc * mass)
