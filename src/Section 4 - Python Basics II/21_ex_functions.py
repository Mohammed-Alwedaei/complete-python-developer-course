# Exercise: find the highest even value in a list

my_list = [10, 8, 7, 9, 11, 12]


def highest_even(list):
    """
    info: finds the highest even number in a given list
    return: number
    """
    max = 0

    for value in list:
        if value % 2 == 0 and value > max:
            max = value

    return max


print(f"The highest even in the list is {highest_even(my_list)}")
