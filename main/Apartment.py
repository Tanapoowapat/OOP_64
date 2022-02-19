from Property import Property
class Apartment(Property):

    def __init__(self, balcony, laundry, **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry
    
    def display(self):
        super().display()
        print(f'Apartment Have Balcony : {self.balcony}')
        print(f'Apartment Have Laundary : {self.laundry}')

    @staticmethod
    def prompt_init():
        property_init = Property.prompt_init()
        balcony = input("Apartment have Balcony ? : ")
        laundry = input("Apartment have Laundry ? : ")

        property_init['Balcony'] = balcony
        property_init['laundey'] = laundry
    
        return property_init
