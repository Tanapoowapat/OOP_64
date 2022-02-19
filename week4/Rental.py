class Rental():
    def __init__(self, furnished, rent):
        self.furnished = furnished
        self.rent = rent
    
    def display(self):
        print(f'Furnished : {self.furnished}')
        print(f'Rent Price : {self.rent}')
        print('****************************************')

    @staticmethod
    def prompt_init():
        furnished = input("Enter Furnished : ")
        rent = input("Enter Rent Price : ")
        data = {}
        data['Furnished'] = furnished
        data['Rent'] = rent

        return data
