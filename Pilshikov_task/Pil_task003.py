#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

Task 1.18  page 8
write formula

"""
import math


def formula_task_pilshikov_1_18(number: int) -> float:
    """
    This function calculate by formula from task Pilshikov
    :param number: type integer
    :return: number type float
    """
    return math.pow(math.pow(number, 8) + math.pow(8, number), 1 / 8)


enter_number = int(input("Calculated formula  - (x^2 + 8^x)^8/2\nEnter integer x: "))
print("Answer:", formula_task_pilshikov_1_18(enter_number))
