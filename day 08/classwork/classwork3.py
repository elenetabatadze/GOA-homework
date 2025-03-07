user_input = input("Enter a word: ")


reversed_string = ""


for i in user_input:
    reversed_string = i + reversed_string


print("Reversed word:", reversed_string)