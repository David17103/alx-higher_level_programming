#!/usr/bin/python3
# This script defines a function for adding integers.

def add_integer(a, b=98):
    """
    Calculate the sum of two numbers and return the result as an integer.

    If the input numbers are floats, they are converted to integers before addition.

    Parameters:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The integer sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

