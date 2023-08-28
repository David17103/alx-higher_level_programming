#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """Executes the function safely.

    Args:
        fct: The function to be executed.
        args: Arguments for the fct.

    Returns:
        If an error happens - None.
        Otherwise - the results of call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)

