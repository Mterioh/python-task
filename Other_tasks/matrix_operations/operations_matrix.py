#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

Operations with matrix

"""


def sum_diagonal_matrix(matrix: list) -> int:
    """
    This function calculate sum diagonals matrix (general case)
    :param matrix: nested list (matrix MxN)
    :return: sum diagonal matrix
    """
    index_matrix = len(matrix)
    result = 0
    for i in range(index_matrix):
        result += matrix[i][i]
    return result


def composition_diagonal_matrix(matrix: list) -> int:
    """
    This function calculate sum diagonals matrix (general case)
    :param matrix: nested list (matrix MxN)
    :return: sum diagonal matrix
    """
    result = 0
    index_matrix = len(matrix)
    for i in range(index_matrix):
        result *= matrix[i][i]
    return result


def additions_matrix(matrix_one: list, matrix_two: list) -> list:
    """
    This function additions 2 matrix (general case)
    :param matrix_one: matrix MxN
    :param matrix_two: matrix MxN
    :return: sum matrix
    """
    rows_count = len(matrix_one)
    columns_count = len(matrix_two[0])
    for i in range(rows_count):
        for j in range(columns_count):
            matrix_one[i][j] += matrix_two[i][j]
    return matrix_one


def transpose_matrix(matrix: list) -> list:
    """
    This function transpose matrix (general case)
    :param matrix: matrix size MxN (quadratic)
    :return: transpose matrix
    """
    result = []
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    for j in range(columns_count):
        row = []
        for i in range(rows_count):
            row = row + [matrix[i][j]]
        result = result + [row]
    return result


def multiplication_matrix(matrix_one: list, matrix_two: list) -> list:
    """
    This function multiplications matrix (general case)
    :param matrix_one: matrix size MxN
    :param matrix_two: matrix size MxN
    :return: result multiplication matrix
    """
    rows_count = len(matrix_one)
    columns_count = len(matrix_two[0])
    element = []
    result = []
    for i in range(rows_count):
        for j in range(columns_count):
            count = 0
            for k in range(rows_count):
                count += (matrix_one[i][k] * matrix_two[k][j])
            element.append(count)
        result.append(element)
        element = []
    return result

