import math

def function(x):
    return x**2 + 4*x

def diff(x):
    return 2*x + 4

alpha = 0.1
x = float(input("Enter value of x:"))

while abs(diff(x)) >= 0.001:
    x = x - alpha * diff(x)
    print(f"Value of x: {x}")

print(f"Final value of x: {x}")
