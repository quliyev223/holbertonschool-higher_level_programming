#!/usr/bin/python3
"""Module 2-matrix_divided

This module provides a function `matrix_divided` which divides all elements
of a matrix by a given number, returning a new matrix with rounded values.
It also validates the input matrix and divisor.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The divisor.

    Returns:
        list: New matrix with elements divided by div, rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of numbers or row
        s differ in size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if (not isinstance(matrix, list)
            or not all(isinstance(row, list) for row in matrix)
            or not all(
                isinstance(x, (int, float)) for row in matrix for x in row
            )):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [
        [round(el / div, 2) for el in row]
        for row in matrix
    ]
    return new_matrix
