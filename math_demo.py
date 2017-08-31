#this program demonstrates how to use the math module
#
#alex fossum
#august 31, 2017

import math

#the math module has constants
print(math.pi)
print(math.e)

#the math module also has built in functions

print(math.sqrt(2))
print(math.sin(.5))

def triangle_area(b,h):
    a=(1/2)*b*h
    return a

def circle_area(r):
    a=(math.pi)*r**2
    return a

#function calls

print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))


