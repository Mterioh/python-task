#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

Task 3.19 page 18
are any of the digits of a three-digit number the same

"""


def check_number_digit(number):
    """check number of digit"""
    return len(str(number)) == 3


def divides_number(number):
    """divides the number by the digits"""
    digit_series = []
    while number > 0:
        digit_series.append(number % 10)
        number //= 10
    return digit_series


input_number = int(input("This program are any of the digits of a three-digit number the same\nEnter numb: "))

while True:
    """Recursive function call to check a number"""
    check_number = check_number_digit(input_number)
    if check_number:
        break
    else:
        check_number = check_number_digit(input_number)
        input_number = int(input("Please, enter a three-digit number: "))

# Call function divides_number
revers_digit_series = divides_number(input_number)
# turning list
revers_digit_series[::-1]
# search duplicate numbers
print('Yes' if revers_digit_series[0] == revers_digit_series[1] \
               or revers_digit_series[1] == revers_digit_series[2] \
               or revers_digit_series[2] == revers_digit_series[0] else 'No')
