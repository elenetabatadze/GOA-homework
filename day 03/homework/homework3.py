score = int(input("Enter your score: "))  # მომხმარებლის ქულის შეყვანა

if score > 90:
    grade = "A"
elif score > 75:
    grade = "B"
elif score > 60:
    grade = "C"
elif score > 50:
    grade = "D"
elif score > 40:
    grade = "E"
else:
    grade = "F"

print("Your grade is:", grade)