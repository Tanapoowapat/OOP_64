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
        parent_init = Property.prompt_init()
        garage = input('garage : ')
        fenced_yard = input('fenced_yard : ')
        parent_init['Garage'] = garage
        parent_init['Fenced yard'] = fenced_yard

        return parent_init
