#!/usr/bin/python3

def number_of_lines(filename=""):
    try:
        with open(filename, "r", encoding="UTF-8") as f:
            return len(f.readlines())
    except FileNotFoundError:
        return 0

