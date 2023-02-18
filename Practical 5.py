# Python program to find the circumference and area of a circle with a given radius

import math

radius = float (input("Enter radius: "))

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print("The circumference of the circle is:", circumference)
print("The area of the circle is:", area)
