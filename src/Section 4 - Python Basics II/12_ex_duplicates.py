# solution:
# loop over the characters array and check if the charcater count
# is greater than 1
# if true add it to the dplicates list

my_list = ["a", "b", "c", "d", "d", "c"]

duplicates = []

for char in my_list:
    if my_list.count(char) > 1:
        if char not in duplicates:
            duplicates.append(char)

print(duplicates)
