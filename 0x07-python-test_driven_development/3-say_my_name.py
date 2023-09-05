#!/usr/bin/python3
# This script defines a function for printing names.

def say_my_name(first_name, last_name=""):
    """
    Print a name with the given first and last names.

    Args:
        first_name (str): The first name to print.
        last_name (str, optional): The last name to print (default is an empty string).

    Raises:
        TypeError: If either first_name or last_name are not strings.
    """
    # Check if both first_name and last_name are strings.
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    # Print the formatted name.
    print("My name is {} {}".format(first_name, last_name))

