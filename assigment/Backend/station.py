from Backend.constants import PackgesStatus
from Backend.employee import Employee
from Backend.search import Search
from Backend.package import Package

class Station(Search):
    All_station_list = []
    def __init__(self, id_station, name, station_address):
        self.__employee_list = []
        self.__packageslist = []
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
    def packageslist(self):
        return self.__packageslist

    @property
    def employee_list(self):
        return self.__employee_list
    
    @property
    def packages_list(self):
        return self.__packageslist

    def add_employee(self, employee):
        if len(self.employee_list) == 0:
            self.employee_list.append(employee)
            return True
        for employee_details in self.employee_list:
            if employee_details.accout.username == employee.accout.username or employee_details.name == employee.name:
                return False
            else:
                self.employee_list.append(employee)
                return True

    def get_employee(self, username):
        for employee in self.employee_list:
            employee.fetch_details()
            if employee.username == username:
                return employee

    def add_packages(self, packages):
        if len(self.packageslist) == 0:
            self.packageslist.append(packages)
            return True
        for item in self.packageslist:
            if item.id == packages.id:
                return False
            else:
                self.packageslist.append(packages)
                return True

    
    def search_packages(self, packges_id):
        for packges in self.packageslist:
            if packges.id == packges_id:
                return super().search_packages(packges)

    def transfer_station(self, packages):
        for package in self.__packageslist:
            if package.id == packages.id:
                transfer_pack  = self.__packageslist.pop(package.id-1)
                return transfer_pack

    def get_package(self, id):
        for package in self.packages_list:
            if package.id == id:
                return package 

    @staticmethod
    def get_station(station_id):
        for station in Station.All_station_list:
            if station_id == station.station_id:
                return station

    def __str__(self):
        return self.station_id

# station = Station('1', 'BKK01', 'SomeWhere')
# station.get_packages(Employee.create_package('1', 'somewhere', 'BIG', 'test', '18.00'))



# #print(station.packageslist)
# #station.search_packages('1')