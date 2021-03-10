#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

max number in list numbers

"""

import random


def max_list_numbers(series_numbers: list) -> int:
    """
    This function find max numbers in list
    :param series_numbers: list numbers
    :return: number type integer
    """
    return max(series_numbers)


def random_list_numbers() -> list:
    """
    This function create list of 10 random numbers
    :return: list random numbers
    """
    series_number = []
    for i in range(11):
        series_number.append(random.randint(0, 100))
    return series_number


# Call function for create random list numbers
random_numbers = random_list_numbers()

print("Max number in random series number: ", max_list_numbers(random_numbers))
