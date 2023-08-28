#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    If a ValueError message is found, a corresponding
    message will be printed to a standard error.

    Args:
        value (int): The integer to be printed.

    Returns:
        If a TypeError or ValueError happens - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)

