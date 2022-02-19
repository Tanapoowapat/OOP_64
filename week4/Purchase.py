class Purchase:
    def __init__(self, price):
        self.price = price


    def display(self):
        print(f'Purchase Info')
        print(f'Price : {self.price}')
        print("="*30)

    @staticmethod
    def prompt_init():
        data = {}
        validate = True
        
        while validate == True:
            
            price = input('Enter Price : ')

            if price.isnumeric():

                data['Price'] = price
                validate = False

            else:
                print("Invalid Input")
                
        return data
