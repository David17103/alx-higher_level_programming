#!/usr/bin/python3
"""Defines a class square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the new square.

        Args:
            size (int): The size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of square."""
        return (self.__size * self.__size)

