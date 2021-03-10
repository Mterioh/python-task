#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

Task 1.14  page 8
write formula

"""
import math


def formula_task_pilshikov_1_14(number: int) -> float:
    """
    This function calculate value due to description in Pilschikov book, task 1.14, page 8
    :param number: type integer
    :return: number type float
    """
    return math.pow((1 + number), 2)


enter_number = int(input('Calculated formula  - (1+x)^2\nEnter integer x: '))
print('Answer:', formula_task_pilshikov_1_14(enter_number))
