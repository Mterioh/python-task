#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

Task 3.19 page 18
condition for the existence of a triangle

"""


def existence_triangle(x: int, y: int, z: int):
    """
    This function calculate value due to description in Pilschikov book, task 3.19, page 18
    :param x: side triangle x type integer
    :param y: side triangle y type integer
    :param z: side triangle z type integer
    """
    if (x < y + z) and (y < x + z) and (z < x + y):
        print('Yes')
    else:
        print('No')


enter_x = int(input("This program condition for the existence of a triangle\nenter side x: "))
enter_y = int(input("enter side y: "))
enter_z = int(input("enter side z: "))
