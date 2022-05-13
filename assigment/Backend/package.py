from Backend.record_package import Record_Package
from Backend.constants import *

class Package:
    P_id = 1
    def __init__(self, id_customer, destination, station_id, size_type, package_status, time):
        self.__p_id = Package.P_id
        self.__id_customer = id_customer
        self.__destination = destination
        self.__size = size_type
        self.__status = package_status
        self.__time =  time
        self.__record = Record_Package()
        self.__station_id = station_id
        Package.P_id += 1
    
    def fetch_details(self):
        print("Packges Details")
        print(f'Packges ID : {self.id}')
        print(f'Destination : {self.destination}')
        print(f'Size : {self.__size}')
        print(f'Status : {self.status}')
        print(f'Status : {self.station_id}')
        print(f'record : {self.record.record}')
        print(f'Time : {self.__time}\n')
        print("="*20)
    
    @property
    def record(self):
        return self.__record

    @property
    def size(self):
        return self.__size
    @property
    def customer_id(self):
        return self.__id_customer

    @property
    def id(self):
        return self.__p_id

    @property
    def station_id(self):
        return self.__station_id

    @station_id.setter
    def station_id(self, new_station):
        self.__station_id = new_station

    @property
    def id_cus(self):
        return self.__id_customer

    @property
    def destination(self):
        return self.__destination

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        self.__status = new_status

    def save_record(self):
        return self.__record.save_record(self.P_id, self.id_customer, self.destination, self.Size, self.Status, self.Time)

    def __str__(self):
        return f"Package ID : {self.id}\nCustomber ID : {self.customer_id}\nStation :{self.station_id}\nDestination : {self.destination}\n{self.status}\nTime : {self.__time}"