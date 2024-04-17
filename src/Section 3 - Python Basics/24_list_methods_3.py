# list methods:
#  - copy() -> returns a copy of the list
#  - sort() -> sorts the list asc
#  - reverse() -> reverse the order of the list

# list functions
#  - sorted(iterable) -> return a sorted list

cart = [ 'grape', 'watermelon', 'dragon fruit' ]

# sort and reverse the list
cart.sort()
cart.reverse()

my_cart = cart.copy()

print(sorted(my_cart))