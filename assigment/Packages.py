from constant import *


class AllPackges:
    
    @staticmethod
    def fecth_details() :
        return Packages

class Recive_Packges:
    recive_packges_list =  []
    

class Deliver_Package:
    deliver_package_list = []

class Successfully_Package:
    Successfully_Package_list = []
    



class Packages():
    packges_list = []
    packges_id = 1
    def __init__(self, customer, postal_address, time, size, employee):
        self.__p_id = Packages.packges_id
        self.__customer_details = customer
        self.__postal_address = postal_address
        self.__time = time
        self.__size = size
        self.__respnsible = employee

        Packages.packges_id += 1

    @property
    def get_details(self):
        return self.__p_id, self.__customer_details, self.__postal_address, self.__time, self.__size, self.__respnsible

    
    def fecth_details(self):
        print("Packges Details")
        print(f"Packges ID : {self.__p_id}")
        print(f"{self.__customer_details}")
        print(f"Address : {self.__postal_address}")
        print(f"Time since last update : {self.__time}")
        print(f"Packges Size : {self.__size}")
        print(f"Respnsible Employee : {self.__respnsible}")
        
