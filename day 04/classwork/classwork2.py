number = int(input("Please enter a number: "))

if number > 0:
    res = 1
elif number < 0:
    res = -1
else:
    res = 0
print("res =", res)

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

# Find and print the largest number
if num1 > num2:
    print("The largest number is:", num1)
else:
    print("The largest number is:", num2)