from Backend.customer import Customer
from Backend.package import Package
from Backend.constants import *
from Backend.employee import Employee
from Backend.accout import Person
from Backend.station import Station


class  Admin(Person):
    All_admin_list = [] 
    def __init__(self, name, phone, accoutType, username, password, accoutStatus):
        super().__init__(name, phone, accoutType, username, password, accoutStatus)

    def fetch_details(self):
        return super().fetch_details()

    def get_admin(username):
        for admin in Admin.All_admin_list:
            admin.fetch_details()
            if admin.username == username:
                return admin


    @staticmethod
    def create_employee(postalbranch, name, phone, username, password, accoutType):
            try:
                station = Station.get_station(postalbranch)
                if station.add_employee(Employee(name, phone, username, password, accoutType)):
                    return True
                else:
                    return False
            except AttributeError:
                return False
    
    @staticmethod
    def update_employee(station_id, username, new_status):
            try:
                station = Station.get_station(station_id)
                for employee in station.employee_list:
                        if employee.accout.username == username:
                            employee.accout.status = new_status
                            return True
            except AttributeError:
                return False

    @staticmethod
    def create_station(id_station, name, station_address):
        if len(Station.All_station_list) == 0:
            Station.All_station_list.append(Station(id_station, name, station_address))
        else:
            for station in Station.All_station_list:
                if station.name == name or station.station_id == id_station:
                    return False
                else:
                    Station.All_station_list.append(Station(id_station, name, station_address))
                    return True


Admin.All_admin_list.append(Admin('Tavan', '99999999', AccoutType.Admin,'admin', '1234', AccoutStatus.Active))
Admin.All_admin_list.append(Admin('Tanapoowapat', '99999999', AccoutType.Admin,'hunter00211', 'gamesinw001', AccoutStatus.Active))




# Admin.All_admin_list.append(Admin('Tanapoowapat', '99999999', AccoutType.Admin,'hunter00211', 'gamesinw001', AccoutStatus.Active))

#Employee.All_Employee_list.append(Employee('jack', '12312314', '12313', 'emp01', '1234', AccoutType.Employee, AccoutStatus.Active))
# admin.update_employee(1, AccoutStatus.Out)

Admin.create_station('BKK01', 'Bankok Sukhumvit', '60 Sukhumvit 95/1 Bang Jark Phra Khanong')
Admin.create_station('BKK02', 'Bankok Bang Phongphang ', 'Bang Phongphang Yan Nawa')
Admin.create_station('BKK03', 'Bankok Vanich', '432 Vanich 1 Road Samphanthawong')
Admin.create_station('BKK04', 'Bankok Samsen', '68-70 Samsen Road Banpanthom')
Admin.create_station('BKK05', 'Bankok Pracharaj Sai ', '801 Soi 23 Pracharaj Sai 1 Bang Sue Bang Sue')
Admin.create_station('BKK06', 'Bankok Pathum Wan', 'Rong Muang Pathum Wan')

station = Station.get_station('BKK01')

Admin.create_employee('BKK01', 'Som Jean', '0999999999', 'user1', '1234', AccoutType.Employee)
Admin.create_employee('BKK01', 'LOL', '0999999999', 'user2', '1234', AccoutType.Employee)
Admin.create_employee('BKK01', 'SAM', '0999999999', 'user3', '1234', AccoutType.Employee)

Employee.create_customer('160991251561', 'Bradly', '088315657489', AccoutType.Customer, 'test', '1234', AccoutStatus.Active)


station.add_packages(Employee.create_package('56822', '4789 Biddie Lane Richmond 23227', station.station_id, SizeType.Big, PackgesStatus.Deliver, '08.00'))
station.add_packages(Employee.create_package('12578', 'someWhere', station.station_id, SizeType.Big, PackgesStatus.Deliver, '08.00'))
station.add_packages(Employee.create_package('20145', 'someWhere', station.station_id, SizeType.Big, PackgesStatus.Deliver, '08.00'))
station.add_packages(Employee.create_package('98745', 'someWhere', station.station_id, SizeType.Big, PackgesStatus.Deliver, '08.00'))
station.add_packages(Employee.create_package('46162', 'someWhere', station.station_id, SizeType.Big, PackgesStatus.Deliver, '08.00'))

# pack = station.search_packages(1)

# Employee.update_package(pack, "BKK02", PackgesStatus.Deliver)
# Employee.update_package(pack, "BKK02", PackgesStatus.Deliver)
# Employee.update_package(pack, "BKK02", PackgesStatus.Deliver)
# Employee.update_package(pack, "BKK02", PackgesStatus.Deliver)
# Employee.update_package(pack, "BKK02", PackgesStatus.Deliver)
# Employee.update_package(pack, "BKK02", PackgesStatus.Deliver)

customer = Customer('56822', 'Jack', '0882683318', AccoutType.Customer, 'jack1234', '1234', AccoutStatus.Active)