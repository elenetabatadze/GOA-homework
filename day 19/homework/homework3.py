def count_positives_and_sum_negatives(list1, list2):
    combined = list1 + list2
    positive_count = 0
    negative_sum = 0

    for num in combined:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_sum += num

    return positive_count, negative_sum

a = [14, -23, 333, -42]
b = [-90, 54, -61]

result = count_positives_and_sum_negatives(a, b)
print("dadebiti ricxvebi", result[0])
print("uaryopiti ricxvebi:", result[1])