from Property import Property

class Apartment(Property):
    def __init__(self, square_feet, num_bedroom, num_bathroom, balcony, laundry):
        super().__init__(square_feet, num_bedroom, num_bathroom)
        self.balcony = balcony
        self.laundry = laundry

    def __str__(self):
        return

    def display(self):
        super().display()
        print(f'Have Balcony : {self.balcony}\nLaundary: {self.laundry}')

    def prompt_init():
        parent_init = Property.prompt_init()
        balcony = input('Enter Balcony : ')
        laundary = input('Enter laundary : ')
        parent_init['Balcony'] = balcony 
        parent_init['Laundary'] = laundary
        #my_ap = Apartment(parent_init)
        #return my_ap
        return parent_init