from Property import Property

class House(Property):



    def __init__(self, square_feet, num_bedroom, num_bathroom, garage, fenced_yard):
        super().__init__(square_feet, num_bedroom, num_bathroom)
        self.garage = garage
        self.fenced_yard = fenced_yard

    def display(self):
        super().display()
        print(f'Garage : {self.garage}')
        print(f'Fenced Yard : {self.fenced_yard}')

    @staticmethod
    def prompt_init():
        valid_data = ("y","n")
        parent_init = Property.prompt_init()
        validate_data = True
        
        while validate_data == True:

            garage = input('garage (y/n): ').lower()
            if garage in valid_data:
                fenced_yard = input('fenced_yard (y/n): ').lower()
                if fenced_yard in valid_data:
                    parent_init['Garage'] = garage
                    parent_init['Fenced yard'] = fenced_yard
                    validate_data = False
                else:
                    print("Invalid Input")
            else:
                print("Invalid Input")

        return parent_init
        