# polymoriphism means many forms


# Parent class used to log players in
class Player(object):

    def sign_in(self):
        print(f"A new player is logged in")

    def attack(self):
        print(f"The player has started attacking")


# A derived class for a player of type Archer
class Archer(Player):

    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        Player.attack(self)
        print(f"Attacking with {self.arrows} arrows...")


# A derived class for a player of type Goblin
class Goblin(Player):

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with {self.power}...")


archer = Archer("Robin", 100)
goblin = Goblin("Ginger", 50)


# applying polymoriphism
def player_attack(player):
    player.attack()


# calling the player attack function
# player_attack(archer)
# player_attack(goblin)

players = [archer, goblin]

for player in players:
    player.attack()
