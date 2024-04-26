# create a lambda expression that square the numbers in the list


my_list = [5, 4, 3]

print(f"The squared list is {list(map(lambda number: number * number, my_list))}")


# sort a list of tuples acsendingly

unsorted_list = [(0, 2), (4, 3), (9, 9), (10, -1)]

unsorted_list.sort(key=lambda item: item[1])

print(f"The sorted list is {unsorted_list}")
