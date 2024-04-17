# sets methods:
#  - difference(set) -> returns the difference in a set and b set
#  - difference_update(set) -> returns the difference in a set and b set and updates a set
#  - intersection(set) -> returns the items in a set and b set
#  - isdisjoint(set) -> returns a boolean indicating if the sets are not joint
#  - issubset(set) -> returns a boolean indicating if a set is a subset of b set
#  - issuperset(set) -> returns a boolean if a set is the super set of b set
#  - union(set) -> returns merged set of a set and b set

a_set = {1, 2, 3, 4, 5}
b_set = {4, 5, 6, 7, 8}

print(a_set.difference(b_set))

c_set = a_set.difference_update(b_set)

print(c_set)

print(a_set.intersection(b_set))

# will work if there is common values in a set and b set

print(a_set.isdisjoint(b_set))

# will work if all values of a set is part of b set

print(a_set.issubset(b_set))

print(b_set.issuperset(a_set))

print(a_set.union(b_set))
