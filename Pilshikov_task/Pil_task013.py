#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

delete excess  symbols and search symbols 'k', 'e', 'y'

"""


def delete_excess_symbols(words: str):
    """
    This function delete excess symbols in enter string
    :param words: type string
    :return: string without duplicate characters
    """
    empty_string = ''
    for element_word in words:
        if element_word not in empty_string and element_word != ' ':
            empty_string += element_word
    return empty_string


def search_in_blank_line(words: str):
    """
    This function search specific letters
    :param words: type string
    """
    # call function clean enter string
    empty_string = delete_excess_symbols(words)
    counter_existing_letters = 0
    for index_empty_string in range(len(empty_string)):
        for index_existing_letters in range(len(EXISTING_LETTER)):
            if empty_string[index_empty_string] == EXISTING_LETTER[index_existing_letters]:
                counter_existing_letters += 1
    return counter_existing_letters


def result(counter: int):
    """
    :param counter: number type integer
    """
    if counter == 3:
        print('Yes')
    else:
        print('No')


enter_word = input("This program search in enter string symbols 'k', 'e', 'y'\n"
                   "Please enter string: ")
EXISTING_LETTER = 'key'
result(search_in_blank_line(enter_word))
