#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

Task 1.1  page 7
calculating the factorial

"""


def calculate_factorial(number: int) -> int:
    """
    This function calculates factorial of entered number
    :param number: type integer
    :return: factorial number type integer
    """
    result = 1
    for number_series_element in range(result, number + 1):
        result *= number_series_element
    return result


enter_number = int(input("Enter an integer to calculate factorial: "))
answer = calculate_factorial(enter_number)
print('Factorial = ', answer)
