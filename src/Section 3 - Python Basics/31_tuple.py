# a tuple is an immutable data structure

items = (1, 2, 3, 4)

print(items)

# tuples can be used in dictionary keys unlike lists
# this behaviour is because of the immutability of the tuples
# unlike lists

dictionary = {"a": [1, 2, 3], (1, 2): True}

print(dictionary[(1, 2)])
