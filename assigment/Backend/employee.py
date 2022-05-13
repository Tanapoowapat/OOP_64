from Backend.accout import Person
from Backend.customer import Customer
from Backend.constants import *
from Backend.package import Package
import datetime

class Employee(Person):
    All_Employee_list = []

    def __init__(self, name, phone, username, password, accoutType):
        super().__init__(name, phone, accoutType, username, password, accoutStatus=AccoutStatus.Active)

    def fetch_details(self):
        return super().fetch_details()

    @staticmethod
    def create_customer(c_id, name, phone, accoutType, username, password, accoutStatus):
        if len(Customer.All_Customer_list) == 0:
            Customer.All_Customer_list.append(Customer(c_id, name, phone, accoutType, username, password, accoutStatus))
            return True
        else:
            Customer.All_Customer_list.append(Customer(c_id, name, phone, accoutType, username, password, accoutStatus))


    @staticmethod
    def sucess_packges(package):
        Customer.recceive_Package(package)
        return True

    @staticmethod
    def update_package(package, new_station, new_status):
        package.station_id = new_station
        package.status = new_status
        time = datetime.datetime.now()
        package.record.save_record(package.id, package.id_cus, package.destination, package.size, package.status, time)
        if package.status == PackgesStatus.Sucessfully:
            print('bar')
            Employee.sucess_packges(package)
        else:
            return package



    @staticmethod
    def create_package(id_customer, destination, station_id, size_type, package_status, time):
        return Package(id_customer, destination, station_id, size_type, package_status, time)