#Define animal class

class Animal():

# Class is a cookie cutter for objects.
    # wraps its characteristics and its behaviours

# Define some chracteristics/attributes/properties/variables
# age has been set to a default value of 0. defaults need to go as the last argument.
    def __init__(self, eyes, legs, age = 0):
        self.bones = True
        self.alive = True
        self.age = 0
        self.number_eyes = eyes
        self.number_legs = legs
#Define some behaviours/methods/functions -
    # Things an instance of an object can do
    # functions that are dependant on an object type.

    def eat(self):
        return 'Nom Nom Nom'

    def mating(self):
        return ' <3 '

    def mate_calling(self):
        return ' Swipe Right'

    def sleep(self):
        return 'zzzzz'



simba = Animal(2, 4, 10)





