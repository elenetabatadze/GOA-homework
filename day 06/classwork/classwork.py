num = int(input("please enter your number"))
count = 0
for i in range(2,num):
    if num % i == 0 and count == 0:
        print("your number is not a prime")
        count += 1
