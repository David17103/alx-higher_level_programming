#!/usr/bin/python3
"""
Module with the method is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """Method that will return True if an object is an instance of a class
    that inherited from"""

    return isinstance(obj, a_class)
