#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

Task 2.10 page 12
х ∈ [0,1] ?

"""

input_numb = float(input("Enter number type - float,to check the condition\n х ∈ [0,1] ?: "))
# checking the condition
print('Yes' if 0 < input_numb < 1 else 'No')

