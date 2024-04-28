# decorators in Python implements the decorator pattern
# its prefferable to use the *args and **kwargs

# example


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("********")
        func(*args, **kwargs)
        print("********\n")

    return wrapper


@my_decorator
def greet(greeting, emoji="):"):
    print(greeting, emoji)


greet("Hello User", "(:")
