# to loop over a dictionary you can use on of the following methods:
#  - items()
#  - keys()
#  - values()

user = {"name": "Golen", "age": 5000, "can_swim": False}

# method one

for item in user.items():
    key, value = item
    print(key, value)

# method two

for key in user.keys():
    print(key)

# method three

for value in user.values():
    print(value)

# method four

for key, value in user.items():
    print(key, value)
