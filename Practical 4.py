# Python program to find the product of a set of real numbers

nums = input("Enter the set of numbers separated by spaces: ")


nums = [float(num) for num in nums]

product = 1

for num in nums:
    product *= num

print("Product of the set of numbers is:", product)
