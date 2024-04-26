# set and dict comprehensions are quite the same as list comporehensions
# the difference is in the {...vals} and {...key:vals}

# set
my_set = {1, 2, 3}

my_new_set = {number**2 for number in my_set}

print(my_new_set)

# dict

my_dict = {"a": 1, "b": 2}

my_new_dict = {key: val**2 for key, val in my_dict.items() if val % 2 == 0}

print(my_new_dict)

# assign the key and value from lists

my_new_dict2 = {number: number**2 for number in [1, 2, 3]}

print(my_new_dict2)
