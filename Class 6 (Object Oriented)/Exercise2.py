coinPoints = 0
potionPoints = 0
totalPoints = 0

class Collectible:
    totalPoints = 0

    def __init__(self,name):
        self.name = name

class Coin(Collectible):
    coinPoints = 0

    def points(self):
        self.coinPoints += 10
        Collectible.totalPoints += 10

class Potion(Collectible):
    name = "Potion"
    potionPoints = 0

    def __init__(self, colour):
        self.colour = colour.lower()

    def points(self):
        if self.colour == "green":
            if self.potionPoints > 100:
                self.potionPoints -= 100
                Collectible.totalPoints -= 100
            else:

        else:
            self.potionPoints += 50
            Collectible.totalPoints += 50

print("You've found a coin")
# Coin.points()