# enumrate returns an enumrate object that contains

for index, char in enumerate("hello, mohammed"):
    print(f"the index of {char} is {index}")

for index, item in enumerate(range(100)):
    if item == 50:
        print(f"the index of item 50 is {index}")
