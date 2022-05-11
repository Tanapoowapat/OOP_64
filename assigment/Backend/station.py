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

    @property
    def employee_list(self):
        return self.__employee_list
    
    def add_employee(self, employee):
        if employee in self.employee_list:
            return False
        else:
            self.employee_list.append(employee)
            return True

    def get_employee(self):
        pass




    def add_packages(self, packages):
        if len(self.packages_list) == 0:
            self.packages_list.append(packages)
            return True
        for item in self.packages_list:
            if item.id == packages.id:
                return False
            else:
                self.packages_list.append(packages)
                return True

    def search_packages(self, packges_id):
        print('search packages call')
        for packges in self.packges_list:
            if packges.id == packges_id:
                return super().search_packages(packges)

    @staticmethod
    def get_station(station_id):
        for station in Station.All_station_list:
            if station_id == station.station_id:
                return station


# station = Station('1', 'BKK01', 'SomeWhere')
# station.get_packages(Employee.create_package('1', 'somewhere', 'BIG', 'test', '18.00'))
# for package in station.packages_list:
#     package.fetch_details()

# #print(station.packages_list)
# #station.search_packages('1')