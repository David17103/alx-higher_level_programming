#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    num_arguments = len(argv)

    print("{} argument{}{}".format(num_arguments, 's' if num_arguments != 1 else '',
        ':' if num_arguments > 0 else '.'))

    for i, arg in enumerate(argv, start=1):
        print("{} {}".format(i, arg))
