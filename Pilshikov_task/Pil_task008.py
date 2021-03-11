#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

Task 3.19 page 18
are any of the digits of a three-digit number the same

"""


def check_number_digit(number: int) -> bool:
    """
    check number of digit
    :param number: type integer
    :return: True if condition is met, else False
    """
    return len(str(number)) == 3


def divides_number(number: int) -> list:
    """
    divides the number by the digits
    :param number: type integer
    :return: list digits
    """
    digit_series = []
    while number > 0:
        digit_series.append(number % 10)
        number //= 10
    return digit_series


def search_duplicate_number(digits: list):
    """
    :param digits: type list
    """
    if digits[0] == digits[1] or digits[1] == digits[2] \
            or digits[2] == digits[0]:
        print('Yes')
    else:
        print('No')


enter_number = int(input("This program are any of the digits of a three-digit number the same\nEnter numb: "))

while True:
    """Recursive function call to check a number"""
    check_entered = check_number_digit(enter_number)
    if check_entered:
        break
    else:
        check_entered = check_number_digit(enter_number)
        enter_number = int(input("Please, enter a three-digit number: "))

# Call function divides_number
list_digit = divides_number(enter_number)
search_duplicate_number(list_digit[::-1])
