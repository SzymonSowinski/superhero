import random

class super_bohater():
    def __init__(self, data):
        self.name = "Suprman"
        self.superpowers = ['oczy', "rece"]
        self.life_points = random.randint(1, 10)

    def attack(self):
        return random.randint(1, 10)


    def decrease_life(self, x ):
        self.life_points = max(self.life_points - x)


super_bohater_1 = super_bohater()