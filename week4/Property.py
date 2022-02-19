class Property(object):
    id_counter = 0
    def __init__(self, square_feet, num_bedroom, num_bathroom) :     
        self.square_feet = square_feet
        self.num_bedroom = num_bedroom
        self.num_bathroom = num_bathroom
        Property.id_counter += 1
        self.id = Property.id_counter

    def display(self):
        print('='*30)
        print(f'Property ID : {self.id}')
        print(f'Sqaure feet : {self.square_feet}')
        print(f'Number of Bedroom : {self.num_bedroom}')
        print(f'Number of Bathroom : {self.num_bathroom}')
        


    @staticmethod
    def prompt_init():
        data = {}

        validate = True
        while validate:

            square_feet = (input('Enter Squre Feet : '))
            if square_feet.isnumeric():
                num_bedroom = (input('Enter Number of Bedroom : '))
                if num_bedroom.isnumeric():
                    num_bathroom = input('Enter Number of Bathroom : ')
                    if num_bathroom.isnumeric():
                        data["Square Feet"] = square_feet
                        data["Number of Bedroom"] = num_bedroom
                        data["Number of Bathroom"] = num_bathroom
                        validate = False

                    else:
                        print('invalid Input')
                else:
                    print('Invalid Input')
            else:
                print("Invalid Input")

        return data
