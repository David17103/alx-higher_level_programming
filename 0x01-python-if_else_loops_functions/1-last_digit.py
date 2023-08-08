#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit_last = abs(number) % 10
if number < 0:
    digit_last = -digit_last

print("Last digit of {} is {}".format(number, digit_last), end=" ")

if digit_last > 5:
    print("and is greater than 5")
elif digit_last == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
