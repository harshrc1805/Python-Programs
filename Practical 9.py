# Python program to find the geometric mean of n numbers

import math

nums = [2, 4, 6, 8, 10]

product = 1

for num in nums:
    product *= num

geometric_mean = math.pow(product, 1/len(nums))

print("The geometric mean of the numbers is:", geometric_mean)
