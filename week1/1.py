class VendingMachine:
    def __init__(self, id, ven_money):
        self.id = id
        self.ven_money = ven_money
        self.item_list = []

    def add_item(self, product_list):
        for i in product_list:
            self.item_list.append(i)

    def view_item(self):
        return self.item_list

class Product:
    def __init__(self, name, product_type, qty, price):
        self.name = name
        self.product_type = product_type
        self.qty = qty
        self.price = price
        self.product = []
        

    def get_product(self):
        self.product.append([self.name , self.product_type, self.qty, self.price])
        return self.product

Coke = Product("Coke", "Drink", 5, 20)
Pepsi = Product("Pepsi", "Drink", 5, 19)
VendingMachine_A = VendingMachine(1, 2000)

VendingMachine_A.add_item(Pepsi.get_product())
VendingMachine_A.add_item(Coke.get_product())

print(VendingMachine_A.view_item())