class Purchase:
    def __init__(self, Price, **kwargs):
        super().__init__(**kwargs)
        self.price = Price

    def display(self):
        super().display()
        print("Purchase Info")
        print(f'Price : {self.price}')

    def prompt_init():
        data = {}
        price = int(input("House Price : "))
        data['Price'] = price
        return data
