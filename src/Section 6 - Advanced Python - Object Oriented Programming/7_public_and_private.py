# A private field is prefixed with underscore (_)
# since python does not have built-in functionality for public/private.


class Player:
    # class attributes
    membership = False

    # name and age are private attributes
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print(f"{self._name} is running...")


player1 = Player("James", 31)

player1.run()
