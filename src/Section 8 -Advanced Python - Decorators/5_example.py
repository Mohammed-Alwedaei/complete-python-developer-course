# performance decorator to measure the execution time

from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()

        result = fn(*args, **kwargs)

        t2 = time()

        print(f"It took {t2 - t1}s")

        return result

    return wrapper


@performance
def my_func():
    for number in range(100000000):
        number * 3


my_func()
