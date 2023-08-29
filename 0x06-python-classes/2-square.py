#!/usr/bin/python3
"""Defines a class square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the new Square.

        Args:
            size (int): The size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

