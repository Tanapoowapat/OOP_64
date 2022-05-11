from employee import Employee
from search import Search
from package import Package
from constants import *


class Station(Search):
    All_station_list = []
    def __init__(self, id_station, name, station_address):
        self.__employee_list = []
        self.__package_list = []
        self.__id_station = id_station
        self.__station_name = name
        self.__station_address = station_address

    @property
    def name(self):
        return self.__station_name

    @property
    def station_id(self):
        return self.__id_station
    
    @staticmethod
    def get_station(station_id):
            for station in Station.All_station_list:
                if station.station_id == station_id:
                    return station
            
    def add_employee(self, employee):
        station = Station.get_station()
        if len(self.employee_list) == 0:
            self.employee_list.append(employee)
            return True
        else:
            for station_employee in self.employee_list:
                if station_employee.name == employee.name:
                    return False
                else:
                    self.employee_list.append(employee)
                    return True

    @property
    def package_list(self):
        return self.__package_list
    
    @property
    def employee_list(self):
        return self.__employee_list
    
    def add_package(self, id_customer, destination, station_id, size_type, package_status, time):
        package = Employee.create_package(id_customer, destination, station_id, size_type, package_status, time)
        if package in self.package_list:
            print("Station alredaay have package")
        else:
            self.package_list.append(package)

    def search_package(self, package_id):
        # print('search package call')
        for package in self.package_list:
            if package.id == package_id:
                return super().search_package(package)
            else:
                return False

    def transfer_package(self, package_id, new_station_id, new_status):
        new_station = Station.get_station(new_station_id)
        print(new_station.station_id)
        # for package in self.package_list:
        #     if package.id == package_id:
        #         Employee.update_package(package, new_station, new_status)

station = Station.All_station_list.append(Station('BKK01', 'Bankok', 'somewhere'))
station = Station.All_station_list.append(Station('BKK02', 'Bankok', 'somewhere'))


print(Station.All_station_list)
# station.add_employee(Employee('jack', '1234', 'user1', '1234', AccoutType.Employee))
# station.add_package('1', 'somewhere', 'BKK01', SizeType.Small, PackgesStatus.Deliver, '08.00')
#station.transfer_package(1, 'BKK02', PackgesStatus.Sucessfully)

