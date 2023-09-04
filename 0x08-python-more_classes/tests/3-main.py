#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(repr(my_rectangle))
print(str(my_rectangle))

print("--")

my_rectangle.height = 3
my_rectangle.width = 10
print(my_rectangle)
print(repr(my_rectangle))
