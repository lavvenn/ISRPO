import math

def area(a: float, b: float, c: float) -> float:
    """Площадь треугольника по формуле Герона"""
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Треугольник с такими сторонами не существует")
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def perimeter(a: float, b: float, c: float) -> float:
    """Периметр треугольника"""
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Треугольник с такими сторонами не существует")
    return a + b + c