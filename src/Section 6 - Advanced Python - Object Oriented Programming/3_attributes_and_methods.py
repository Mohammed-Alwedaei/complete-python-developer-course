# A class attribute is property of the class that hold a data about the instance
# A class method is a grouped logic that hold an executable code


class Player:
    # class attributes
    membership = True

    def __init__(self, name, age):
        if self.membership:
            self.name = name
            self.age = age
        else:
            self.name = "Anonymous"
            self.age = 0

    def run(self):
        return f"{self.name} is running..."


player1 = Player("Ali", 95)

print(player1.run())
