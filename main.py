import random
class Human:
    def __init__(self, name = "Human", job = None, home = None):
        self.name = name
        self.job = job
        self.money = 100
        self.gladness = 50
        self.sateity = 50
        def get_home(self):
            self.home = House()
        def get_food(self):
            if self.home.food <= 0:
                self.shopping = 'food'
            elif self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5
        def get_bycicle = Bucicle(color_of_bycicle)
        def get_home(self):
            self.home = House()

class Bycicle:
    def __init__(self, color_of_bycicle):
        self.color_of_bycicle = ["red", 'green', 'blue']
        if choce(self.color_of_bycicle) == 'red':
            self.color_of_bycicle = 'red'
        else choce(self.color_of_bycicle) == 'green':
            self.color_of_bycicle = 'green'
        else:
            self.color_of_bycicle = 'blue'










class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
        self.ecological = 0

