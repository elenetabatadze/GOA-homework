def manual_reverse(s):

    reversed_str = ''
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str
print(manual_reverse("tabatadzeelene"))
