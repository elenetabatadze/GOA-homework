def merge_and_sort_lists(list1, list2):
    merged_list = list1 + list2
    merged_list.sort()
    return merged_list

a = [900, 0, 90, 90]
b = [90, 73, 333]

result = merge_and_sort_lists(a, b)
print(result) 