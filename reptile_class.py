from animal_class import *

class Reptile(Animal):

    def __init__(self, eyes, legs, n_chamber_heart, age = 0):
        super().__init__(eyes, legs, age)
        self.scales = True
        self.cold_blood = True
        self.n_chamber_heart = 4

    def mate_calling(self):           # This is our example of polymorphism
        return 'Look at my scales.'

    def seek_heat(self):
        return 'It is cold'

    def seek_shade(self):
        return 'It is too hot'

    def prey(self):
        return 'Time to eat'

    def lay_eggs(self):
        return 'Time to lay mu egg babies'