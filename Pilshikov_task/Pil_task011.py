#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

prime divisors of a number

"""


def prime_divisors_number(number: int):
    """
    This function outputs list  all prime divisors of a number
    :param number: type integer
    :return:
    """
    for element_number_series in range(1, number + 1):
        if number % element_number_series == 0:
            all_prime_divisors.append(element_number_series)


all_prime_divisors = []
enter_numb = int(input("This program defines all prime divisors number\nEnter numb: "))
prime_divisors_number(enter_numb)
print("List prime defines -", all_prime_divisors)
