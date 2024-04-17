# dictionary methods
#  - pop(key) -> pops a key from the dictionary
#  - popitem() -> randomly pops a key from the dictionary
#  - clear() -> removes all key-value pairs from the list
#  - update({}) -> update an existing key or add it of none
#  - items() -> returns the items in a tuple data structure inside a list (dict_items)

dictionary = {"a": [1, 2, 3], "b": True, "c": 9584, "x": True}

print(dictionary.items())

print(dictionary.pop("a"))

print(dictionary.popitem())

dictionary.clear()

dictionary.update({"xy": False})

print(dictionary)
