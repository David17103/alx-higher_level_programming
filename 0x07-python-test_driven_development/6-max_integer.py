#!/usr/bin/python3
"""Defines a function to find the maximum integer in a list."""


def max_integer(list=[]):
    """Find and return the maximum integer in a list of integers.

    Args:
        list (list, optional): A list of integers. Defaults to an empty list.

    Returns:
        int or None: The maximum integer in the list or None if the list is empty.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

