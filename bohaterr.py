import random

class super_bohaterr():
    def __init__(self, data):
        self.name = "Batman"
        self.superpowers = ['szurikan', "batobil"]
        self.life_points = random.randint(1, 10)

    def attack(self):
        return random.randint(1, 10)


    def decrease_life(self, x ):
        self.life_points = max(self.life_points - x)


super_bohater_2 = super_bohaterr()