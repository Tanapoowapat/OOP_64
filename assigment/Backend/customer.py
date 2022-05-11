class Customer():
    All_Customer_list = []
    def __init__(self, C_id, name, phone, accountType):
        # super().__init__(name, phone, accountType)
        self.__c_id = C_id
        self.__package_list = []

    def show_history(self):
        for pack in self.package_list:
            print(pack)
    
    @property
    def id(self):
        return self.__c_id
    
    @id.setter
    def id(self, new_id):
        self.__c_id = new_id



    @staticmethod
    def recceive_Package(Package):
        for customer in Customer.All_Customer_list:
            if customer.C_id == Package.id :
                customer.package_list.append(Package)