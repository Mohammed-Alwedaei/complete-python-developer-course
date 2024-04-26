# multiple inheritance is inheriting from multiple classes


# Parent class used to log players in
class Player(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print(f"A new player is logged in")


# A derived class for a player of type Archer
class Archer(Player):

    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrow(self):
        print(f"Attacking with {self.arrows} arrows...")


# A derived class for a player of type Goblin
class Goblin(Player):

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with {self.power}...")


class Hybrid(Archer, Goblin):
    def __init__(self, name, arrows, power):
        Archer.name = name
        Archer.arrows = arrows
        Goblin.power = power


hybrid = Hybrid("Hybridie", 50, 100)

hybrid.check_arrow()
hybrid.attack()
