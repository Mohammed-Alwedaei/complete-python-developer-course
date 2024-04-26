# A class method decorator (@classmethod) is used to indicate a method is owned by a class object
# The paramaters are (cls, params)

# A static method decorator (@staticmethod) is used to indicate that a method
# is available within the class itself.
# And there are no params in this decorator


class Player:
    # class attributes
    membership = False

    def __init__(self, name, age, power):
        if self.membership:
            self.name = name
            self.age = age
            self.power = power

    def run(self):
        return f"{self.name} is running..."

    @classmethod
    def attack(cls, power):
        return cls("Ali", 15, power)

    @staticmethod
    def walk(speed):
        return f"The speed is {speed}"


player1 = Player.attack(15)

print(Player.walk(6))
