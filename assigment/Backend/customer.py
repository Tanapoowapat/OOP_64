class Customer():
    All_Customer_list = []
    def __init__(self, C_id, name, phone, accountType):
        # super().__init__(name, phone, accountType)
        self.C_id = C_id
        self.package_list = []

    def show_history(self):
        for pack in self.package_list:
            print(pack)
    
    @staticmethod
    def recceive_Package(Package):
        for obj_cus in Customer.All_Customer_list:
            if obj_cus.C_id == Package.ID_Customer :
                obj_cus.package_list.append(Package)