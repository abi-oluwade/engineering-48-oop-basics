from animal_class import *
from reptile_class import *

# Creating an instance of Animal class
simba = Animal(2, 5, 5)
ringo = Reptile(2, 5, 6)

print(simba)
print(simba.sleep())
print(simba.mating())

#Calling methods on an object
print(simba.eat())
print(simba.age)

# Call the attributes of an object
print(simba.bones)
print(simba.number_legs)
