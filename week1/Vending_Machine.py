class VendingMachine:
    def __init__(self, id, ven_money):
        self.id = id # id ของตู้กดสินค้า
        self.ven_money = ven_money #จำนวนเงินที่มีอยู่ในตู้กดสินค้า
        self.item_list = [] #สินค้าที่แสดงในตู้

    def add_item(self, product_list):
        for i in product_list:
            self.item_list.append(i)

    def show_stock(self):
        return self.item_list

    def buy_product(self, product_name, buy_qty, customer_money):
        for i in range(len(self.item_list)):
            if i+2 > len(self.item_list):
                break
            elif product_name == self.item_list[i][0]:
                self.item_list[i][2] = self.item_list[i][2] - buy_qty
                self.ven_money += buy_qty*self.item_list[i][3]
                customer_money += buy_qty*self.item_list[i][3]
                return product_name, buy_qty, customer_money
                

class Product:
    def __init__(self, name, product_type, qty, price):
        self.name = name #ชื่อสินค้า
        self.product_type = product_type #ประเภทสินค้า
        self.qty = qty #จำนวนสินค้า
        self.price = price #ราคา
        self.product = [] #เอาไว้รวม Attribute ทั้งหมด

    def get_product(self):
        self.product.append(
            [self.name, self.product_type, self.qty, self.price])
        return self.product


class Customer:
    def __init__(self, name, money):
        self.name = name #ชื่อลูกค้า
        self.money = money #เงินของลูกค้า
        self.item_list = [] #ที่เก็บของ ของลูกค้าเมื่อซื้อสินค้าเสร็จ

    def order_product(self, product_name, qty):
       self.item_list = list(VendingMachine_A.buy_product(product_name, qty, self.money))

    def __str__(self):
        return f'ชื่อ : {self.name} \nจำนวนเงินคงเหลือ : {self.item_list[2]-self.money} \nมีของอยู่ในกระเป๋ามี : {self.item_list[0]} \nจำนวน : {self.item_list[1]} '

Customer_1 = Customer("ตะวัน", 70)
Customer_2 = Customer("ธนภูวภัสสร์", 20)

Coke = Product("Coke", "Drink", 5, 20)
Lae = Product("Lae", "Snack", 5, 19)
Sink = Product("Sink", "Drink", 20, 49)

VendingMachine_A = VendingMachine(1, 2000)

VendingMachine_A.add_item(Lae.get_product())
VendingMachine_A.add_item(Coke.get_product())
VendingMachine_A.add_item(Sink.get_product())

Customer_1.order_product("Coke", 2)
print(f'\n{Customer_1}\n')

print(VendingMachine_A.item_list[0][0])
print(Coke.name)

print('\n')

VendingMachine_A.item_list[1][2] = 20 #เปลี่ยนจำนวนสินค้าในตู้กด
Customer_1.item_list[0] = "Lae" #เปลี่ยนชื่อสินค้าจาก Coke เป็น Lae

print(VendingMachine_A.show_stock())
print(Customer_1.item_list)