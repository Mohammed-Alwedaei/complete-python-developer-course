# a function parameter can be declared with a default value


def printer(name="Ali", age=19):
    print(f"My name is {name} and I am {age} years old")


printer()

# a function parameters can be added using keyword parameters

printer(name="Hasan", age=35)
