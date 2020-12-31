# x^3 - 1

a = 7
h = 0.000001

Fah = (a+h) * (a+h) * (a+h) - 1
Fa = a * a * a - 1

derivative = (Fah - Fa) / h
print(derivative)
