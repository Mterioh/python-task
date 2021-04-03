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
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                result += matrix[i][j]
    return result


def composition_diagonal_matrix(matrix: list) -> int:
    """
    This function calculate sum diagonals matrix (general case)
    :param matrix: nested list (matrix MxN)
    :return: sum diagonal matrix
    """
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                result *= matrix[i][j]
    return result


def additions_matrix(matrix_1: list, matrix_2: list, M: int, N: int) -> list:
    """
    This function additions 2 matrix (general case)
    :param matrix_1: nested list (matrix MxN)
    :param matrix_2: nested list (matrix MxN)
    :param M: size string
    :param N: size column
    :return: sum matrix
    """
    result = [[0 for element_M in range(M)] for element_N in range(N)]
    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[0])):
            result[i][j] = matrix_1[i][j] + matrix_2[i][j]
    return result


def transpose_matrix(matrix: list) -> list:
    """
    This function transpose matrix (general case)
    :param matrix: matrix size MxN (quadratic)
    :return: transpose matrix
    """
    result = []
    main_list = len(matrix)
    nested_list = len(matrix[0])
    for j in range(nested_list):
        temp_matrix = []
        for i in range(main_list):
            temp_matrix = temp_matrix + [matrix[i][j]]
        result = result + [temp_matrix]
    return result


def multiplication_matrix(matrix_one: list, matrix_two: list) -> list:
    """
    This function multiplications matrix (general case)
    :param matrix_one: matrix size MxN
    :param matrix_two: matrix size MxN
    :return: result multiplication matrix
    """
    temp_matrix = []
    result_matrix = []
    for i in range(len(matrix_one)):
        for j in range(len(matrix_two[0])):
            sums = 0
            for k in range(len(matrix_two)):
                sums = sums + (matrix_one[i][k] * matrix_two[k][j])
            temp_matrix.append(sums)
        result_matrix.append(temp_matrix)
        temp_matrix = []
    return result_matrix