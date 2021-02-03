"""Heat calculations"""


def calculate_heat_amount(shc: float, mass: float, temperature: float) -> float:
    """Calculate heat amount based on heat capacity, mass and temperature"""
    return shc * mass * temperature
