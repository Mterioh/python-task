#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

list of negative numbers

"""


def check_negative_number(number):
    """This function defines negative number"""
    return number < 0


def recording_negative_number(number):
    """This function recording negatives numbers in list 'numbers_series'"""
    if check_negative_number(number):
        negative_numbers.append(number)


# List negative numbers
negative_numbers = []
# Counter enter the numbers
counter = 0
input_number = int(input("This program defined list negative numbers\n"
                         "Enter 5 integer number: "))
# Recursive call enter variables
while counter != 4:
    counter += 1
    input_number = int(input())
    # Call function recording_negative_number
    recording_negative_number(input_number)

print("List negative numbers ->", negative_numbers if len(negative_numbers) != 0 else "This list no negative  numbers")
