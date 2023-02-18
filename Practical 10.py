#Python program to find the roots of a quadratic equation

import math

a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("The roots are complex.")
else:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)

    print("The roots are", root1, "and", root2)

