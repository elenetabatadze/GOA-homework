def list_with_greater_sum(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    
    if sum1 > sum2:
        return list1
    elif sum2 > sum1:
        return list2


a = [22, 80]
b = [1, 40]

result = list_with_greater_sum(a, b)
print(result)