# lambda expression is an anonymous function that will be called
# only once

from functools import reduce

my_list = [1, 2, 3, 4]

print(f"The even numbers are {list(filter(lambda item: item % 2 == 0, my_list))}")

print(f"The sum of the numbers is {reduce(lambda acc, item: acc + item, my_list, 0)}")
