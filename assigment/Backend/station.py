from employee import *
from search import Search

class Station(Search):
    All_station_list = []
    def __init__(self, id_station, name, station_address):
        self.__employee_list = []
        self.__packages_list = []
        self.__id_station = id_station
        self.__station_name = name
        self.__statino_address = station_address

    @property
    def name(self):
        return self.__station_name

    @property
    def station_id(self):
        return self.__id_station

    @property
    def packges_list(self):
        return self.__packages_list

    def get_employee(self, employee_name):
       if employee_name in Employee.All_Employee_list:
           print(employee_name)

    def search_packages(self, packges_id):
        for packges in self.packges_list:
            if packges.id == packges_id:
                return super().search_packages(packges)

