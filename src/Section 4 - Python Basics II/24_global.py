# global keyword is used to access no identation variables


a = 10


def find_num():
    global a
    a += 1
    return a


find_num()
find_num()
print(find_num())

# global keyword can lead to a chaotic codebase
# rather use dependency injection

b = 10


def find_sum_better(number):
    number += 1
    return number


print(find_sum_better(find_sum_better(find_sum_better(b))))
