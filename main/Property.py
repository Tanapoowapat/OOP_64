class Property:
    id_counter = 0
    def __init__(self, Square_Feet, Number_Bedroom, Number_Bathroom, **kwargs):
        super().__init__(**kwargs)
        self.square_feet = Square_Feet
        self.num_bedroom = Number_Bedroom
        self.num_bathroom  = Number_Bathroom
        Property.id_counter += 1
        self.id = Property.id_counter


    def display(self):
        print('====Property====')
        print(f'Property ID : {self.id}')
        print(f'Square Feet : {self.square_feet}')
        print(f'Number of Bedroom : {self.num_bedroom}')
        print(f'Number of Bathroom : {self.num_bathroom}')

    @staticmethod
    def prompt_init():
        square_feet = int(input("Enter Square Feet : "))
        num_bedroom = int(input("Number of Bedroom : "))
        num_bathroom = int(input("Number of Bathroom : "))
        
        data = {}
        data["Square_Feet"] = square_feet
        data["Number_Bedroom"] = num_bedroom
        data["Number_Bathroom"] = num_bathroom
        
        return data