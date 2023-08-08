#!/usr/bin/python3
for numbers in range(10):
    for single_digit in range(numbers + 1, 10):
        print("{:02d}".format(numbers * 10 + single_digit), end="")
        if single_digit != 9 or single_digit != 8:
            print(", ", end="")
        else:
            print()
