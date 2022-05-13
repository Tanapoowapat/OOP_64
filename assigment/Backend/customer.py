from Backend.accout import Person, Accout

class Customer(Person):
    All_Customer_list = []
    def __init__(self, c_id, name, phone, accoutType, username, password, accoutStatus):
        super().__init__(name, phone, accoutType, username, password, accoutStatus)
        self.__c_id = c_id
        self.__package_list = []

    @property
    def package_list(self):
        return self.__package_list

    def show_history(self):
        for pack in self.package_list:
            return pack

    @property
    def c_id(self):
        return self.__c_id

    def get_customer(self, id):
        if id == self.c_id:
            return True


    @staticmethod
    def get_customer(username):
        for customer in Customer.All_Customer_list:
            customer.fetch_details()
            if customer.username == username:
                return customer

    @staticmethod
    def recceive_Package(Package):
        print(Package.id)
        for customer in Customer.All_Customer_list:
            if customer.C_id == Package.id :
                customer.package_list.append(Package)

    def __str__(self):
        return  self.c_id