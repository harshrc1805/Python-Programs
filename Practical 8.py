#Python program to display the given integer in a reverse manner

num = int (input("Enter integer:  "))

num_str = str(num)

num_str_reversed = num_str[::-1]

num_reversed = int(num_str_reversed)

print("The reversed integer is: ", num_reversed)
