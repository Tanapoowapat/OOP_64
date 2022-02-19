class Rental:

    def __init__(self, Furnished, Rent, **kwargs):
        super().__init__(**kwargs)
        self.furnished = Furnished
        self.rent = Rent
        print(f'Furnished : {self.furnished}')
        print(f'Rent : {self.rent}')


    def display(self):
        super().display()
        print("Rental Info ")
        print(f'Furnished : {self.furnished}')
        print(f'Rent : {self.rent}')

    def prompt_init():
        data = {}
        furnished = input('Have a Furnished : ')
        rent = int(input("Rental Price : "))
        print('='*30)
        data['Furnished'] = furnished
        data['Rent'] = rent

        return data