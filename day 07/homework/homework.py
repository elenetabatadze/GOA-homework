num = int(input("enter number: "))


divisors = []
for i in range(1, num + 1):
    if num % i == 0:  
        divisors.append(i)

# გამყოფების გამოშვება (თითოეული გამყოფი ცალ-ცალკე)
for divisor in divisors:
    print(divisor)