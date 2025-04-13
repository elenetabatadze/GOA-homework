def manual_remove(lst, value):
    ricxvebi = []
    for item in lst:
        if item != value:
            ricxvebi.append(item)
    return ricxvebi

original = [99, 48, 31, 43, 32,]
result = manual_remove(original, 32)
print(result)