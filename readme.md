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
- Encapsulation ==	Hiding the private details of a class from other objects.
- Polymorphism == A concept of using common operation in different ways for different data input.
- Abstraction ==

Other learning outcomes:
- Git and GitHub
- Documentation with Markdown
- Best practises and organisation

- CLASS = the class can be seen as the blueprint or schematic of the object, and would hold all the details about the
size,colour,height etc. so in the example below, Abi is the object. classes contain objects, and objects are comprised
of functions and variables that are related.
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
 these objects will also hold (methods/behaviours/functions)

 [  id         ]         [     make     ]
 [  hair       ]         [     model    ]
 [  height     ]         [    colour    ]
 [  skin_tone  ]         [  horsepower  ]     (These would be the 'objects' of different things)
 [-------------]         [ ------------ ]
 [ intro_self()]         [  start_car() ]
 [             ]         [              ]


 - Example:
 class Person:

    - Below is a custom constructor that we can used to account for things such as typos, it will stop the default
    constructor from working. good practise to name arguments to the attributes
    
    def __init__(self, Name, Height, Colour):
        self.name = Name
        self.height = Height  # this block of code sets the objects attribute/properties to the corresponding argument
        self.colour = Colour

     (this is the default constructor when the function is within a class you need to add the argument 'self')
    
    def introduce_self(
            self):
        [print(
            "my name is " + self.name + ", I am " + self.height + " and my favourite colour is " + self.colour + ".")]
         'self' = 'this' in java and will refer to whatever 'object' we are running
         this function on, so for example if th object name is "Tom" it will print "Tom"


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