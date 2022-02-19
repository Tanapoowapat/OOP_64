class Rental():
    def __init__(self, furnished, rent):
        self.furnished = furnished
        self.rent = rent
    
    def display(self):
        print("Rental Info")
        print(f'Furnished : {self.furnished}')
        print(f'Rent Price : {self.rent}')
        print("="*30)

    @staticmethod
    def prompt_init():
        validate_data = ('y','n')
        data = {}
        validate = True

        while validate == True:

            furnished = input("Enter Furnished (y/n): ")

            if furnished in validate_data:

                rent = input("Enter Rent Price: ")

                if rent.isnumeric():

                    data['Furnished'] = furnished
                    data['Rent'] = rent
                    validate = False
                    
                else:
                    print("Invalid Input")
            else:
                print("Invalid Input")

        return data
