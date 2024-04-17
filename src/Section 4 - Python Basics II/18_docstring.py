# docstring is used to document a function / method
# using """ my info  """


def find_sum(num1, num2):
    """
    info: return the sum of param num1 and param num2
    """
    return num1 + num2


find_sum(1, 2)

# help function prints the docstring too

print(help(find_sum))

# __doc__ method return the docstring

print(find_sum.__doc__)
