#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

the number is a palindrome?

"""


def is_palindrome(string):
    """This function checking number for palindrome"""
    reversed_string = string[::-1]
    return string == reversed_string


numb = str(input("This program checking number for palindrome\n"
                 "Enter number: "))
check_palindrome = is_palindrome(numb)
print('Yes' if check_palindrome else 'No')
