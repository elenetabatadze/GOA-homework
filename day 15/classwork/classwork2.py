def filter_divisible(numbers, int):
    result = []  
    for num in numbers:
        if num % int == 0:  
            result.append(num)  
    return result
numbers = [1, 23, 165, 2, 3, 92, 10, 34, 911]
int = 3
print(filter_divisible(numbers, int))