# mro stands for Method Resolution Order
# Python uses DFS to traverse the tree
# .mro() method is used to print the traversed path of a tree


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())
