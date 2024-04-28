# functions can be passed as a parameters
# functions are more like a variables, they can be assigned to a variable


def greet():
    print("Hello, Anonymous!")


say_hello = greet()

say_hello


def greet_user(greeting):
    greeting()


greet_user(greet)
