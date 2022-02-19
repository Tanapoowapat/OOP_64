class Purchase:
    def __init__(self, price):
        self.price = price


    def display(self):
        print(f'Price : {self.price}')
    
    @staticmethod
    def prompt_init():
        price = int(input('Enter Price : '))
        data = {}
        data['Price'] = price
        return data
