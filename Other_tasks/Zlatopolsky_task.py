#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

Collection of tasks Zlatopolsky D.M.
task 8.27, page 100

"""


def divisors(upper_bound: int, bottom_line: int) -> list:
    """
    This function find numbers which have exactly 5 divisors
    :param upper_bound: number
    :param bottom_line: number
    :return: number
    """
    result = []
    counter_divisors = 0
    for i in range(bottom_line, upper_bound):
        for j in range(1, i + 1):
            if i % j == 0:
                counter_divisors += 1
        if counter_divisors == 5:
            result.append(i)
        counter_divisors = 0
    return result

