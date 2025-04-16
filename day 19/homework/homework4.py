def remove_divisible_by_3(lst):
    return [num for num in lst if num % 3 != 0]

numbers = [20, 21, 22, 23, 24, 25,26]
result = remove_divisible_by_3(numbers)
print(result)