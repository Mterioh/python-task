#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

enter number / 7?

"""


def checking_condition(number: int) -> str:
    """
    This function checking divisibility of a number by 7
    :param number: enter number type integer
    :return: answer "Yes" or "No"
    """
    return 'Yes' if number % 7 == 0 else 'No'


enter_number = int(input("Enter integer number for verification (input_numb % 7 == 0)?: "))
print(checking_condition(enter_number))
