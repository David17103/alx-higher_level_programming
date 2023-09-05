#!/usr/bin/python3
# This script defines a function for printing a square using '#' characters.

def print_square(size):
    """
    Print a square with '#' characters of the specified size.

    Args:
        size (int): The height and width of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    # Check if size is an integer.
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is non-negative.
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square using '#' characters.
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

