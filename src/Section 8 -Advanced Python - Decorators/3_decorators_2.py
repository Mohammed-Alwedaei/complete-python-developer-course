# to create a decorator create a function that have nested wrapper function
# that calls the function, and then returns the wrapper


# example


def styler(func):
    def wrapper():
        print("********")
        func()
        print("********\n")

    return wrapper


@styler
def greet():
    print("Hello, Anonymous!")


@styler
def bye():
    print("See you!")


greet()
bye()
