import math


def circle_area(radius: float) -> tuple[float]:
    area_1 = 3.14 * radius ** 2
    area_2 = math.pi * radius ** 2
    area_3 = math.pi * math.pow(radius, 2)
    return area_1, area_2, area_3


def rectangle_area(width: float, height: float) -> float:
    return width * height