# list adding methods 
# -> doesn't return anything:
#  - append(val) => adds a value to the end of the list
#  - extend(iterable) => adds a list of items to the list
#  - insert(i?, val) => adds a value to the list (optional: the position of the item)

# list removing methods:
#  - pop(i) => removes the last item in the list (optional: the position of the item) -> return the removed item
#  - remove(val) => removes a value from the list -> doesn't return anything
#  - clear() => clears the list -> doesn't return anything

cart = [ 'notebooks', 'grapes', 'a book' ]

my_cart = cart.clear()

print(cart)