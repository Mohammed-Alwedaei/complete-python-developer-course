# Parent class used to log players in
class Player:

    def sign_in(self):
        print(f"A new player is logged in")


# A derived class for a player of type Archer
class Archer(Player):

    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f"Attacking with {self.arrows} arrows...")


# A derived class for a player of type Goblin
class Goblin(Player):

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with {self.power}...")


# Instantiate objects
archer = Archer("Robit", 30)
goblin = Goblin("Geriger", 100)

# Login players
archer.sign_in()
goblin.sign_in()

# Start players attack
archer.attack()
goblin.attack()
