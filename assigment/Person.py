from accout import Accout
from packages import Packages
from constant import *
from station import All_station, Station

class Person():
    def __init__(self, username, password, status, name, phone, accoutType, postalbranch, email):
        self.__obj_accout = Accout(username, password, status)  
        self.__name = name
        self.__phone = phone
        self.__accoutType = accoutType
        self.__postalbranch  = postalbranch
        self.__email = email
    

    def __str__ (self):
        return f'{self.__obj_accout}\nName : {self.__name}\nPhone Number : {self.__phone}\nAccout Type : {self.__accoutType}\nE-mail : {self.__email}\nPostalBranch : {self.__postalbranch}'

class Employee(Person):

    employee_list = []

    def __init__(self, username, password, name, phone, email, postalbranch, status, accoutType= AccoutType.Employee):
        super().__init__(username, password, status, name, phone, accoutType, postalbranch, email)
    
    @staticmethod
    def create_packges(customer, postal_address, time, size, employee):
        packges = Packages.packges_list.append(Packages(customer, postal_address, time, size, employee))
    
    @staticmethod
    def update_customer():
        pass

    @staticmethod
    def delete_customer():
        pass

class Admin(Person):

    def __init__(self, username, password, name, phone, postalbranch, email, status=AccoutStatus.Active, accoutType=AccoutType.Admin):
        super().__init__(username, password, status, name, phone,accoutType , postalbranch, email)

    @staticmethod
    def create_station():
        name = input("Enter station name : ")
        station = All_station.all_station_list.append()



class Customer(Person):

    customer_list = []

    def __init__(self, username, password, status, name, phone, accoutType, email, address):
        super().__init__(username, password, status, name, phone, accoutType, email, address)
