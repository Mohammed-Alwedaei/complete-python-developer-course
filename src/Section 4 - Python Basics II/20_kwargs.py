# *args is used to add as many args as wanted
# **kwargs is used to add names args

# a rule to follow is to have the following order:
# 1. parameters
# 2. *args
# 3. default paramters
# 4. **kwargs


def find_sum(*args, **kwargs):
    total = 0
    for number in kwargs.values():
        total += number
    return sum(args, total)


print(find_sum(1, 2, 3, 4, num1=10, num2=15))
