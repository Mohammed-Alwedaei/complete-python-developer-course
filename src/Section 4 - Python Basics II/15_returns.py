# functions can return values using return keyword


def find_sum(num1, num2):
    return num1 + num2


total = find_sum(14, 5)

print(total)

# functions can be nested by declaring another function in the function


def find_total(num1, num2):
    def total(n1, n2):
        return n1 + n2

    return total(num1, num2)


print(find_total(150, 13))
