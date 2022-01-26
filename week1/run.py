class VendingMachine:
  def __init__(self, product_type, name, price, qty):
    self.product_type = product_type
    self.name = name
    self.price = price
    self.qty = qty
    self.money = 100

  def __str__(self):
      return f'Product Type : {self.product_type} Product Name : {self.name} Price : {self.price} คงเหลือ {self.qty}'

  def buy_product(self,qt):
    self.qty = self.qty - qt
    self.money = self.money + self.price


class Customer:
  def __init__(self, name, money, Proname, qt):
    self.name = name
    self.money = money
    if Proname == "Coke":
      Coke.buy_product(qt)


Coke = VendingMachine("Drink","Coke",15,10)
Lae = VendingMachine("Snack","Lae",20,10)
Tiger = VendingMachine("Drink","Tiger",20,10)

man = Customer("man", 2000, "Coke", 2)


print(Coke)