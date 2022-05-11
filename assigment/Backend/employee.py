from Backend.accout import Person
from Backend.customer import Customer
from Backend.constants import *
from Backend.package import Package

class Employee(Person):
    All_Employee_list = []

    def __init__(self, name, phone, username, password, accoutType):
        super().__init__(name, phone, accoutType, username, password, accoutStatus=AccoutStatus.Active)

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


    def get_accout(self):
        return self.get_accout()

    @staticmethod
    def sucess_packges(package):
        pass

    @staticmethod
    def update_package(package, new_station_id, new_status):
        package.station_id = new_station_id
        package.status = new_status
        return True


    @staticmethod
    def create_package(id_customer, destination, station_id, size_type, package_status, time):
        return Package(id_customer, destination, station_id, size_type, package_status, time)