from Backend.employee import Employee
from Backend.search import Search
from Backend.package import Package

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
    def packages_list(self):
        return self.__packages_list

    
    def get_employee(self, employee_name):
        employee = self.__employee_list
        if employee_name in employee:
           return employee
    
    def get_packages(self, packages):
        self.packages_list.append(packages)

    def search_packages(self, packges_id):
        print('search packages call')
        for packges in self.packges_list:
            if packges.id == packges_id:
                return super().search_packages(packges)

# station = Station('1', 'BKK01', 'SomeWhere')
# station.get_packages(Employee.create_package('1', 'somewhere', 'BIG', 'test', '18.00'))
# for package in station.packages_list:
#     package.fetch_details()

# #print(station.packages_list)
# #station.search_packages('1')