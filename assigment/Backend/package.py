from Backend.record_package import Record_Package
from Backend.constants import *

#fadlsfl;asdfl;sdlfp

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
        print(f'Packges ID : {self.P_id}')
        print(f'Destination : {self.destination}')
        print(f'Size : {self.Size}')
        print(f'Status : {self.Status}')
        print(f'Time : {self.Time}')
       
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
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        self.__status = new_status

    
    def save_record(self):
        return self.__record.save_record(self.P_id, self.id_customer, self.destination, self.Size, self.Status, self.Time)