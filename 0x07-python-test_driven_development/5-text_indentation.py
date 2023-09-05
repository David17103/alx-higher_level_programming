#!/usr/bin/python3
# This script defines a function for formatting text with indentation.

def text_indentation(text):
    """
    Print the provided text with two new lines after each '.', '?', or ':'.

    Args:
        text (string): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    # Check if text is a string.
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1

