from accout import Person
from customer import Customer
from constants import *
from package import Package

class Employee(Person):
    All_Employee_list = []

    def __init__(self, name, phone, postalbranch, username, password, accoutType):
        super().__init__(name, phone, accoutType, username, password, accoutStatus=AccoutStatus.Active)
        self.postalbranch = postalbranch

    def fetch_details(self, uid):
        return super().fetch_details(uid)

    @staticmethod
    def create_customer(C_id, name, phone):
        if len(Customer.All_Customer_list) == 0:
            Customer.All_Customer_list.append(Customer(C_id, name, phone, AccoutType.Customer))
        else:
            for customer in Customer.All_Customer_list:
                if customer.C_id == C_id:
                    print("Already have Customer")
                else:
                    Customer.All_Customer_list.append(Customer(C_id, name, phone, AccoutType.Customer))

    @staticmethod
    def create_package(ID_Customer, destination, Size_Type, Package_Status, T):
        return Package(ID_Customer, destination, Size_Type, Package_Status, T)