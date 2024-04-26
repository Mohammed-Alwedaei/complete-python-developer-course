# functional programming is all about seperating data
# from logic

# a function must adhere the following rules:
# 1. a function must always return the same input
# 2. a function must not container side-effects


def multiply_by2(numbers):
    my_list = []

    for number in numbers:
        my_list.append(number * 2)

    return my_list


print(multiply_by2([1, 2, 3]))
