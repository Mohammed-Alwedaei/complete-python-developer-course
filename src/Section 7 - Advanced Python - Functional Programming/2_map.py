# map() function executes an action over an iterable item

my_list = [1, 2, 3, 4]


def multiply_by2(item):
    return item * 2


print(f"Old list: {my_list}")
print(f"New list: {list(map(multiply_by2, my_list))}")
