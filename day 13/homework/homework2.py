number = int(input("Enter a number: "))

# Calculating the sum of digits
digit_sum = 0
for digit in str(number):
    digit_sum += int(digit)

# Calculating the remainder
remainder = number % digit_sum

# Printing the result
print(f"Remainder: {remainder}")