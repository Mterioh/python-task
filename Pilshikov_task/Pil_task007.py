#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

Task 3.13 page 16
the area and perimeter of an inscribed polygon in a circle of a given radius

"""


def calculate_square_polygon(quantity_sides: float, side_len: float, radius: float) -> float:
    """
    This function calculate square polygon
    :param quantity_sides: type float
    :param side_len: type float
    :param radius: type float
    :return: square of polygon
    """
    return 0.5 * quantity_sides * side_len * radius


def calculate_perimeter_polygon(side_len: float, radius: float) -> float:
    """
    This function calculate perimeter polygon
    :param side_len: type float
    :param radius: type float
    :return: perimeter of polygon
    """
    return side_len * radius


enter_quantity_sides = float(input("This program calculate square and perimeter polygon\n"
                                   "Enter quantity sides: "))
enter_side_len = float(input("Enter side length: "))
enter_radius = float(input("Enter the radius of the polygon: "))
square = calculate_square_polygon(enter_quantity_sides, enter_side_len, enter_radius)
perimeter = calculate_perimeter_polygon(enter_side_len, enter_radius)
print('Square polygon:', square, "\nPerimeter polygon ", perimeter)
