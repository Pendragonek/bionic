"""Heat calculations"""


def calculate_heat_amount(shc: float, mass: float, temperature: float) -> float:
    """Calculate heat amount based on SHC, mass and temperature"""
    return shc * mass * temperature


def calculate_temperature_delta(shc: float, mass: float, heat_amount: float) -> float:
    """Calculate temperature delta based on SHC, mass and heat transferred"""
    return heat_amount / (shc * mass)


def calculate_combined_temperature(shc1: float, mass1: float, temperature1: float,
                                   shc2: float, mass2: float, temperature2: float) -> float:
    """Calculate combined temperature, the result of mixing two elements temperature"""
    total_heat_amount = calculate_heat_amount(shc1, mass1, temperature1) + calculate_heat_amount(shc2, mass2,
                                                                                                 temperature2)
    return total_heat_amount / (shc1 * mass1 + shc2 * mass2)
