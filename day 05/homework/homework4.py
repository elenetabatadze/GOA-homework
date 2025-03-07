nput_str = input("elene")
result = ""
for char in input_str:
    if char == "A":  # ან შეიძლება ჩაწეროთ char.upper() == "A", თუ დიდ-კუცის მნიშვნელობაც არ სიხშირეა
        result += "A"
print(result)
    