# functions can accept arguments when defined as
# a parameter when declared in the method signature

my_list = ["a", "b", "c", "d", "d", "c"]


def remove_duplicates(list):
    duplicates = []
    for char in list:
        if char not in duplicates:
            duplicates.append(char)

    print(duplicates)


remove_duplicates(my_list)
