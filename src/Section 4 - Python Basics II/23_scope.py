# scope is the declaration of a variable in a space

# the scope order can be defined as follows:
# 1. local scope -> which can be used only in the function
# 2. parent local scope -> which is functions inheriting the scope of the parent
# 3. global scope -> which is known as no indentation scope
# 4. built in functions -> which is the functions built in python

a = 5


def find_sum():
    a = 10  # if not defined it will fallback to the global scope

    def print_number():
        a = 4  # if not defined it will fallback to the local scope
        return a

    return print_number()


print(a)
print(find_sum())
