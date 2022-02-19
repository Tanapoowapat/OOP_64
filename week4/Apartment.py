from Property import Property

class Apartment(Property):
    def __init__(self, square_feet, num_bedroom, num_bathroom, balcony, laundry):
        super().__init__(square_feet, num_bedroom, num_bathroom)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print(f'Have Balcony : {self.balcony}\nLaundary: {self.laundry}')

    @staticmethod
    def prompt_init():
        valid_data = ('y','n')
        parent_init = Property.prompt_init()
        validate_data = True

        while validate_data == True:
            
            balcony = input('Enter Balcony (y/n) : ')
            if balcony in valid_data:
                laundary = input('Enter laundary (y/n) : ')
                if laundary in valid_data:
                    parent_init['Balcony'] = balcony 
                    parent_init['Laundary'] = laundary
                    validate_data = False
                else:
                    print("Invalid Input")

            else:
                print("Invalid Input")

        return parent_init