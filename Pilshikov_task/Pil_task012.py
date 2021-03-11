#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

the number is a palindrome?

"""


def is_palindrome(word: str) -> bool:
    """
    This function checking number for palindrome
    :param word: number type string
    :return: True if condition is met, else False
    """
    reversed_word = word[::-1]
    return word == reversed_word


def result(var):
    """
    :param var: answer
    """
    if var:
        print('Yes')
    else:
        print('No')


enter_word = str(input("This program checking number for palindrome\n"
                       "Enter number: "))
check_palindrome = is_palindrome(enter_word)
vars(check_palindrome)
