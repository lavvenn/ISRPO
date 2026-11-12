import math

def area(radius: float) -> float:
    """Площадь круга"""
    return math.pi * (radius ** 2)

def perimeter(radius: float) -> float:
    """Длина окружности (периметр)"""
    return 2 * math.pi * radius