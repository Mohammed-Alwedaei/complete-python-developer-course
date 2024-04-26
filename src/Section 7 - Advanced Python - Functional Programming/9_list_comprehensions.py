# comprehensions is a simple method to construct new sequences

# create a list of "Hello, World!"

my_list = [char for char in "Hello, World!"]

print(my_list)

# create a list from number 1 to 100

my_list2 = [number for number in range(1, 101)]

print(my_list2)

# create a list of squared numbers from 1 to 100

my_list3 = [number**2 for number in range(1, 100)]

print(my_list3)

# create a list of squared numbers from 1 to 100 only if the sqaured number is even

my_list4 = [number**2 for number in range(1, 100) if number % 2 == 0]

print(my_list4)
