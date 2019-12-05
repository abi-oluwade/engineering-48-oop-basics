  Object Orientated Programming (OOP)
OOP can be used to solve different types of problems in python
An object will have 2 characteristics
1. attributes (property/properties) (variables)
2. behaviour (methods) (functions)
- So I will use myself as an example: Abi
1. Black, brown eyes, 2 hands (attributes)
2. running and singing (behaviour)

In Python, the concept of OOP follows some basic principles:

- Inheritance == A process of using details from a new class without modifying existing class. 
    Ability of classes to inherit behaviours and characteristics of parent class

- Encapsulation ==	Hiding the private details of a class from other objects.

- Polymorphism == A concept of using common operation in different ways for different data input.
    The ability to change the methods and characteristics of instance of child classes.

- Abstraction == The concept of hiding complexity.

Other learning outcomes:
- Git and GitHub
- Documentation with Markdown
- Best practises and organisation
- Add to definitions 

- CLASS = the class can be seen as the blueprint or schematic of the object, and would hold all the details about the
size,colour,height etc. so in the example below, Abi is the object. classes contain objects, and objects are comprised
of functions and variables that are related. It wraps methods and attributes. Classes can init 
many many instances of different objects.
[                ]
[                ]            [OBJECT]
[                ]          [OBJECT]
[     CLASS      ]  ---->  [OBJECT]       (A Class can be made up of many objects.
[                ]           [OBJECT]
[                ]          [OBJECT]
[                ]         [OBJECT]

 - OBJECTS = An object/instance is an instantiation of a class, when a class is defined ONLY the description of the
 object/instance is defined. it is a collection of 'variables' aka 'properties or attributes' and some 'functions'
 aka 'behaviours or methods'. objects can be designed to hold specific info (properties/attributes/variables)
 eg person(object) = id,hair,height, skin_tone
 eg car(object) =make,colour,horsepower
 these objects will also hold (methods/behaviours/functions), can take arguements but can only be 
 used by an instance of its class.

 [             ]         [    model_name   ]
 [  name       ]         [    memory       ]
 [  height     ]         [    fan_type     ]
 [  colour  ]         [  overclockable  ]     (These would be the 'objects' of different things)
 [-------------]         [ --------------- ]
 [ intro_self()]         [  graphic_card() ]
 [             ]         [              ]

- INSTANCE = It is occurrence of an object.
- ATTRIBUTES =  Hold information about our specific object, are set in the def __init__()
function with arguments like any other method.
- __init__()
AKA - Constructor  or intializer
This method runs every time an object is created. So when you do:
````

animal1 = animal('Fred')

````
- SELF = refers to the object.

 - Example 1:
 class Person:

    - (Below is a custom constructor that we can used to account for things such as typos, it will stop the default
    constructor from working. good practise to name arguments to the attributes)
    
    def __init__(self, Name, Height, Colour):
        self.name = Name
        self.height = Height  # this block of code sets the objects attribute/properties to the corresponding argument
        self.colour = Colour

     (this is the default constructor when the function is within a class you need to add the argument 'self')
    
    def introduce_self(
            self):
        print(
            "my name is " + self.name + ", I am " + self.height + " and my favourite colour is " + self.colour + ".")
         ('self' = 'this' in java and will refer to whatever 'object' we are running
         this function on, so for example if th object name is "Tom" it will print "Tom")


 r1 = Person()
 r1.name = "Abi"
 r1.height = str(177) + 'cm'
 r1.colour = "Blue"

 r2 = Person()
 r2.name = "Timmy"
 r2.height = str(174) + 'cm'
 r2.colour = "Purple"

 - These 2 pieces of code do the same as above but are much clearer and you don't have to rewrite the argument names
 each time. They will both create new 'person' 'objects' that are instances/contained in the class.
 
r1 = Person("Abi", str(177) + "cm", "Black")
r2 = Person("Timmy", str(160) + "cm", "Blue")

r1.introduce_self()   (These are two 'objects' created via the code above.)
r2.introduce_self()  

Example 2
class Graphic_Cards:
    def __init__(self, ModelName, Memory, FanType, Overclock):
        self.model_name = ModelName
        self.memory = str(Memory)
        self.fan_type = FanType
        self.overclockable = Overclock

    def graphic_card(self):   # here the graphic_card is object within the class.
        print(
            "Model Name: " + self.model_name + "  " + "Memory: " + self.memory + "GB " + "  " + "Fan Style: " +
            self.fan_type + ", Do you want to OC? : " + " " +
            self.overclockable
         )


g1 = Graphic_Cards("GTX 1080", 8, "Blower", input("Do you want to OC?"))    #g1 is the first object
g2 = Graphic_Cards("R9 270X", 8, "Open Air", input("Do you want to OC?"))   #g2 is the second onbject

g1.graphic_card()
g2.graphic_card()
