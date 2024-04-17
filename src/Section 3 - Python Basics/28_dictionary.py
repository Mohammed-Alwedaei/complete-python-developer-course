# a dictionary is a data structure that contains key-value pairs
# a dictionary is like key-value pairs

dictionary = {"a": [1, 2, 3], "b": True, "c": 9584}

print(dictionary["a"][0])

# a dictionary can be nested in a list

my_list = [
    {"a": [1, 2, 3], "b": True, "c": 9584},
    {"a": [4, 5, 6], "b": True, "c": 8484},
]

print(my_list[1]["a"][2])

# another way to create a dictionary

user = dict(name="ali", age=25)

print(user["name"])
