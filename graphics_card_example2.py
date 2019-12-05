class Graphic_Cards:
    def __init__(self, ModelName, Memory, FanType, Overclock):
        self.model_name = ModelName
        self.memory = str(Memory)
        self.fan_type = FanType
        self.overclockable = Overclock

    def graphic_card(self):   # here the graphic_card is object instance within the class.
        print(
            "Model Name: " + self.model_name + "  " + "Memory: " + self.memory + "GB " + "  " + "Fan Style: " +
            self.fan_type + ", Do you want to OC? : " + " " +
            self.overclockable
         )


g1 = Graphic_Cards("GTX 1080", 8, "Blower", input("Do you want to OC?"))    #g1 is the first object
g2 = Graphic_Cards("R9 270X", 8, "Open Air", input("Do you want to OC?"))   #g2 is the second onbject

g1.graphic_card()
g2.graphic_card()
