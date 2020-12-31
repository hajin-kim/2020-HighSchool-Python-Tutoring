from math import *

# x^3 - 1
def f(x):
    return x**3 - 1

a = 10
h = 0.0000000001

derivative = (f(a+h) - f(a) ) / h
print(derivative)
