# list slicing is getting an item or items from the list

cart = [ 'notebooks', 'grapes', 'a book' ]

# gets a single item

print(cart[0])

# gets a range of items

print(cart[0:2])

# referenced list is affected by the new list if not sliced

# my_cart = cart

# my_cart[0] = 'graphic card'

# print(cart)

# print(my_cart)

# use slicing to copy lists

my_cart = cart[:]

my_cart[0] = 'gpu'

print(cart)

print(my_cart)
