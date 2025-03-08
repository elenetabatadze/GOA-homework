num = int(input("Enter a number (50 or less): "))


while num < 1 or num > 50:
    print("Enter a number (50 or less)")
    num = int(input("The number must be 50 or less! Please try again: "))

for i in range(num, 101, num):
    print(i)