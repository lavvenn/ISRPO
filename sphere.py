import math

def volume(radius: float) -> float:
    """Объем сферы"""
    return (4 / 3) * math.pi * (radius ** 3)

def surface_area(radius: float) -> float:
    """Площадь поверхности сферы"""
    return 4 * math.pi * (radius ** 2)