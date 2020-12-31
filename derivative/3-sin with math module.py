from math import *

# x^3 - 1

a = 1004 * pi
h = 0.000001

Fah = sin(a+h) * sin(a+h) * sin(a+h) - 1
Fa = sin(a) * sin(a) * sin(a) - 1

derivative = (Fah - Fa) / h
print(derivative)
