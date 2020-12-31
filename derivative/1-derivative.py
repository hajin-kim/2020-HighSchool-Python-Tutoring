

# x * x +

a = 3
h = 0.001

Fah = (a+h) * (a+h) * (a+h) - 1
Fa = a * a * a - 1

derivative = ( Fah - Fa ) / h

print(derivative)
