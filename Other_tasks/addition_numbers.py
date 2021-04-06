#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

addition of large numbers

"""


def equalization():
    """
        determine which entered number is greater and equalize the numbers with zeros
    """

    if len(one_list_number) > len(two_list_number):
        quantity_zero = len(one_list_number) - len(two_list_number)
        for i in range(quantity_zero):
            two_list_number.append(0)
    else:
        quantity_zero = len(two_list_number) - len(one_list_number)
        for i in range(quantity_zero):
            one_list_number.append(0)
    operation_addition()


def operation_addition():
    """
        This function adds numbers in a column
    """
    quantity_step = len(one_list_number)
    overhead = 0
    for i in range(quantity_step):
        digit = two_list_number[i] + one_list_number[i] + overhead
        result.append(digit % 10)
        overhead = digit // 10
    result.append(overhead)


number_1 = str(input("Please, enter number 1: "))
number_2 = str(input("Please, enter number 2: "))
# break numbers into numbers and add them to our lists
one_list_number = []
two_list_number = []
result = []

# str to int in lists
i = 1
while i != len(number_1) + 1:
    one_list_number.append(int(number_1[len(number_1) - i]))
    i += 1
i = 1
while i != len(number_2) + 1:
    two_list_number.append(int(number_2[len(number_2) - i]))
    i += 1
