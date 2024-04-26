# dunder methods can be overridden


class Player(object):
    def __init__(self, email):
        self.email = email
        self.my_dict = {"name": "Ali Jassim", "has_pets": True}

    def sign_in(self):
        print(f"A new player is logged in")

    def attack(self):
        print(f"The player has started attacking")

    def __str__(self):
        return "Yeah, I am string"

    def __len__(self):
        return 5

    def __call__(self):
        return "I have been called..."

    def __getitem__(self, item):
        return f"The name is {self.my_dict[item]}"


player = Player("player@gamestore.com")

print(str(player))
print(len(player))
print(player["name"])
