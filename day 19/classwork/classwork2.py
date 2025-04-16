def remove_odds(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

my_list = [89, 90, 70, 98, 578, 900]
print(remove_odds(my_list)) 

def remove_odds(numbers):
    return [num for num in numbers if num % 2 == 0]