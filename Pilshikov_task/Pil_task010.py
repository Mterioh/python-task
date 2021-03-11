#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

list of negative numbers

"""


def check_negative_number(number: int) -> bool:
    """
    :param number: type integer
    :return:True if condition is met, else False
    """
    return number < 0


def recording_negative_number(number: int):
    """
    This function recording negatives numbers in list 'numbers_series'
    :param number: type integer
    """
    if check_negative_number(number):
        negative_numbers.append(number)


def series_negative_number(series_number: list):
    """
    This function defines presence of negative numbers
    :param series_number: list numbers
    """
    if len(series_number) != 0:
        print("List negative numbers ->", series_number)
    else:
        print("This list no negative  numbers")


# List negative numbers
negative_numbers = []
# Counter enter the numbers
counter = 0
enter_number = int(input("This program defined list negative numbers\n"
                         "Enter 5 integer number: "))
# Recursive call enter variables
while counter != 4:
    counter += 1
    enter_number = int(input())
    # Call function recording_negative_number
    recording_negative_number(enter_number)
series_negative_number(negative_numbers)