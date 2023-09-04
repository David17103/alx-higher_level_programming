#!/usr/bin/python3

class Rectangle:
    """the class only creates private instance attributes by taking two arguments.

    Args:
        width (int): horizontal dimension of the rectangle, defaults to 0
        height (int): vertical dimension of the rectangle, defaults to 0

    """
    def __init__(self, width=0, height=0):
        # attribute assigment here engages setters defined below
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int): horizontal dimension of the rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): horizontal dimension of the rectangle

        Attributes:
            __width (int): horizontal dimension of the rectangle

        Raises:
            TypeError: If `value` not an int.
            ValueError: If `value` less than 0.

        """
        if type(value) is not int:
            raise TypeError('width must be integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter.

        Returns:
            __height (int): vertical dimension of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): vertical dimension of the rectangle

        Attributes:
            __height (int): vertical dimension of the rectangle

        Raises:
            TypeError: If `value` not an int.
            ValueError: If `value` less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
