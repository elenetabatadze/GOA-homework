def manual_append(my_list, element):
    my_list[len(my_list):] = [element]

my_list = [90, 2, 30]
manual_append(my_list, 4)
print(my_list)