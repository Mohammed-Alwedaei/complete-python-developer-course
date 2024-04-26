# filter() function is used to filter an iterable item based on a function


my_list = [1, 2, 3, 4]


def is_even(number):
    return number % 2 == 0


print(f"Old list: {my_list}")
print(f"Filtered list: {list(filter(is_even, my_list))}")
