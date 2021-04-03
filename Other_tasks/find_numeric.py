#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

Find a numeric without a pair

"""


def find_number(lst: list):
    """
    This function find a numeric without a pair
    :param lst: list integer numbers
    :return: non-duplicate number
    """
    element = lst[0]
    for i in range(1, len(lst)):
        element = element ^ lst[i]
    print(element)



