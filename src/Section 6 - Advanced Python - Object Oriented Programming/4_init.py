# A default paramters can be added to __init__()


class Player:
    # class attributes
    membership = False

    def __init__(self, name="Anonymous", age=0):
        if self.membership:
            self.name = name
            self.age = age

    def run(self):
        return f"{self.name} is running..."


player1 = Player("Ali", 95)

print(player1.run())
