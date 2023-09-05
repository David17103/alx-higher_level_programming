#!/usr/bin/python3
# This script defines a function for dividing all elements in a matrix.

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a specified divisor.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If the matrix contains non-numeric values.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an integer or a float.
        ZeroDivisionError: If div is 0.

    Returns:
        list: A new matrix representing the result of the division.
    """
    # Check if the matrix is valid, containing only numeric values.
    if (
        not isinstance(matrix, list)
        or matrix == []
        or not all(isinstance(row, list) for row in matrix)
        or not all(
            (isinstance(ele, int) or isinstance(ele, float))
            for ele in [num for row in matrix for num in row]
        )
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows in the matrix have the same size.
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if the divisor is a number (integer or float) and not zero.
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division and round the results to two decimal places.
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]

