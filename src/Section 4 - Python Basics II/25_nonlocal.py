# nonlocal keyword refers to the parent scope


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print(x)

    inner()

    print(x)


outer()
