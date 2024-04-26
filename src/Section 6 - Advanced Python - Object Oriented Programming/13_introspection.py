# doc function is used to list all the accesseable attributes of an object


# Parent class used to log players in
class Player(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print(f"A new player is logged in")

    def attack(self):
        print(f"The player has started attacking")


# A derived class for a player of type Goblin
class Goblin(Player):

    def __init__(self, name, power, email):
        self.name = name
        self.power = power
        super().__init__(email)

    def attack(self):
        print(f"Attacking with {self.power}...")


goblin = Goblin("Ginger", 50, "ginger@ginger.com")


print(dir(goblin))
