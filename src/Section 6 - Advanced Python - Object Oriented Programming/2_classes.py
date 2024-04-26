# A class can be instantiated with a constructor
# A constructor is called once at the creation time of the object
# Self refers to the current class instance


class Player:
    def __init__(self, name):
        self.name = name

    def run():
        print("Running...")

    def attack():
        print("Attacking...")


player1 = Player("Jassim")

print(f"Player 1 name is: {player1.name}")
