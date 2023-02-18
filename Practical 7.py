#Python program to find the average of 10 numbers using while loop

count = 0 
total = 0

while count < 10:
    num = float(input("Enter a number: "))
    total += num
    count += 1

average = total / 10

print("The average of the 10 numbers is:", average)
