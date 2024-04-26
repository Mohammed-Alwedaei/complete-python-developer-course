# reduce() function is used to accumulate a list with an initial value

from functools import reduce

my_list = [1, 2, 3]


def accumulator(acc, item):
    """
    info: the accumulator will sum the accmulate with the item
    return: the sum value
    """

    return acc + item


print(reduce(accumulator, my_list, 0))
