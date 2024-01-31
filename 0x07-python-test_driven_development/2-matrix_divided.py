#!/usr/bin/python3
"""
This module describes the division in a matrix
"""


def matrix_divided(matrix, div):
    """
    A function that divides all the elements of a matrix
    arguments: matrix(list) - a list with all the elements
             : div(int/float) - the divisor
    Raises: TypeError: if matrix is not a list
            TypeError: if f the rows in the matrix are not the same size
            TypeError: if div is not an int or a float
            ZeroDivisionError: if div is 0
    return: the new matrix after division
    """

    if (not isinstance(matrix, list) or matrix == []
            or not all(isinstance(row, list) for row in matrix)
            or not all(isinstance(element, (int, float))
                for element in[number for row in matrix for number in row])):
                raise TypeError("matrix must be a matrix
                        (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x/div, 2), row)) for row in matrix])
