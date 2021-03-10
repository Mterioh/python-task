#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

Task 2.10 page 12
х ∈ [0,1] ?

"""


def checking_condition(number: float) -> str:
    """
    This function checking whether the number is contained in the specified interval
    :param number: type float
    :return: answer "Yes" or "No"
    """
    return 'Yes' if 0 < number < 1 else 'No'


enter_number = float(input("Enter number type - float,to check the condition\n х ∈ [0,1] ?: "))
print(checking_condition(enter_number))
