from Property import Property

class House(Property):
    def __init__(self, Garage, Fenced_Yard, **kwargs):
        super().__init__(**kwargs)
        self.garage = Garage
        self.fenced_yard = Fenced_Yard
    
    def display(self):
        super().display()
        print(f"Have Garage : {self.garage}")
        print(f"Have Fenced Yard : {self.fenced_yard}")

    @staticmethod
    def prompt_init():
        property_init = Property.prompt_init()
        garage = input("The House Have Garage ? : ")
        fenced_yard = input("The House have Fenced Yard ? : ")
        property_init['Garage'] = garage
        property_init['Fenced_Yard'] = fenced_yard

        return property_init
