# super keyword is used to call the constructor of the parent class


# Parent class used to log players in
class Player(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print(f"A new player is logged in")

    def attack(self):
        print(f"The player has started attacking")


# A derived class for a player of type Archer
class Archer(Player):

    def __init__(self, name, arrows, email):
        self.name = name
        self.arrows = arrows
        super().__init__(email)

    def attack(self):
        Player.attack(self)
        print(f"Attacking with {self.arrows} arrows...")


# A derived class for a player of type Goblin
class Goblin(Player):

    def __init__(self, name, power, email):
        self.name = name
        self.power = power
        super().__init__(email)

    def attack(self):
        print(f"Attacking with {self.power}...")


archer = Archer("Robin", 100, "robin@archer.com")
goblin = Goblin("Ginger", 50, "ginger@ginger.com")


print(archer.email)
print(goblin.email)
