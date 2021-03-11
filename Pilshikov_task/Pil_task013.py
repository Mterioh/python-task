#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

delete excess  symbols and search symbols 'k', 'e', 'y'

"""


def delete_excess_symbols(string):
    """This function delete excess symbols in enter string"""
    blank_line = ''
    for element_string in string:
        if element_string not in blank_line and element_string != ' ':
            blank_line += element_string
    return blank_line


def search_in_blank_line(string):
    """This function search specific letters"""
    # call function clean enter string
    blank_line = delete_excess_symbols(string)
    counter_existing_letters = 0
    for index_blank_line in range(len(blank_line)):
        for index_existing_letters in range(len(existing_letters)):
            if blank_line[index_blank_line] == existing_letters[index_existing_letters]:
                counter_existing_letters += 1
    print('Yes' if counter_existing_letters == 3 else 'No')


input_str = input("This program search in enter string symbols 'k', 'e', 'y'\n"
                  "Please enter string: ")
existing_letters = 'key'
search_in_blank_line(input_str)
