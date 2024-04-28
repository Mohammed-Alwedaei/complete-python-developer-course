# higher order functions are functions that accept a function as a parameter
# or a function that returs a function

# example 1


def greet(say_hello):
    say_hello()


def say_hello():
    print("Hello, from say_hello!")


greet(say_hello)

#


def find_sum(num1, num2):
    def sum(num1, num2):
        return num1 + num2

    return sum(num1, num2)


print(find_sum(3, 3))
