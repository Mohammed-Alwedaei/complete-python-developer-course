# Given the below class:
class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Cindy", 10)
cat2 = Cat("Rocket", 5)
cat3 = Cat("Caterina", 3)


# 2 Create a function that finds the oldest cat
def find_oldest(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest child is {find_oldest(cat1.age, cat2.age, cat3.age)} years old")
