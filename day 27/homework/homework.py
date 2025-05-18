
day = input("sjeiyvane dge: ")
month = input("sheiyvane tve: ")
year = input("sheiyvane weli: ")


print(f"tarigi: {day}/{month}/{year}")


password = input("enter password: ")

if len(password) < 8:
    print("password is too short")
else:
    print("password accepted")


 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


max_num = max(num1, num2, num3)
print("The largest number is:", max_num)   


numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

total = sum(numbers)
print("The sum of the numbers is:", total)