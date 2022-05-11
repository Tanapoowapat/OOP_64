from Backend.package import Package
from Backend.constants import *
from Backend.employee import Employee
from Backend.accout import Person
from Backend.station import Station


class Admin(Person):
    All_admin_list = [] 
    def __init__(self, name, phone, accoutType, username, password, accoutStatus):
        super().__init__(name, phone, accoutType, username, password, accoutStatus)

    def fetch_details(self):
        return super().fetch_details()

    def login(self, username, password):
        return super().login(username, password)

    @staticmethod
    def create_employee(postalbranch, name, phone, username, password, accoutType):
        try:
            station = Station.get_station(postalbranch)
            if station.add_employee(Employee(name, phone, username, password, accoutType)):
                print("Employee Add")
            else:
                print('fail')
        except AttributeError as e:
            print(f'{postalbranch} Not Found!')
    
    @staticmethod
    def update_employee(station_id, uid, new_status):
        try:
            station = Station.get_station(station_id)
            for employee in station.employee_list:
                    if employee.uid == uid:
                        employee.status = new_status
                        print("Update!")
                    else:
                        print(f'ID : {uid} Not Found')
        except AttributeError as e: 
            print("Station Not Found!")

    @staticmethod
    def create_station(id_station, name, station_address):
        if len(Station.All_station_list) == 0:
            Station.All_station_list.append(
                Station(id_station, name, station_address))
        else:
            for station in Station.All_station_list:
                if station.name == name:
                    return False
                else:
                    Station.All_station_list.append(Station(id_station, name, station_address))


Admin.All_admin_list.append(Admin('Tavan', '99999999', AccoutType.Admin,'admin', '1234', AccoutStatus.Active))
Admin.All_admin_list.append(Admin('Tanapoowapat', '99999999', AccoutType.Admin,'hunter00211', 'gamesinw001', AccoutStatus.Active))




# Admin.All_admin_list.append(Admin('Tanapoowapat', '99999999', AccoutType.Admin,'hunter00211', 'gamesinw001', AccoutStatus.Active))

#Employee.All_Employee_list.append(Employee('jack', '12312314', '12313', 'emp01', '1234', AccoutType.Employee, AccoutStatus.Active))
# admin.update_employee(1, AccoutStatus.Out)

Admin.create_station('test', 'test', 'somewhere')
Admin.create_station('BKK01', 'Bankok', 'somewhere')

station = Station.get_station('test')

# if admin.create_station('BKK01', 'Bankok', 'somewhere'):
#     print('Create !')
# else:
#     print('Already Create')

Admin.create_employee('BKK01', 'jack', '1234', 'user1', '1234', AccoutType.Employee)
Admin.create_employee('BKK01', 'John', '1234', 'user2', '1234', AccoutType.Employee)
Admin.create_employee('BKK01', 'hee', '1234', 'user3', '1234', AccoutType.Employee)
Admin.create_employee('BKK01', 'pee', '1234', 'user4', '1234', AccoutType.Employee)
Admin.create_employee('BKK01', 'tew', '1234', 'user5', '1234', AccoutType.Employee)
Admin.create_employee('BKK01', 'xx', '1234', 'user6', '1234', AccoutType.Employee)
Admin.create_employee('BKK01', 'kkk', '1234', 'user7', '1234', AccoutType.Employee)

# admin.update_employee('BKK01', 2, AccoutStatus.Out)

# station.add_packages(Employee.create_package('1', 'somewhere', 'BKK01', SizeType.Big, PackgesStatus.Deliver, '08.00'))

# admin.create_employee('test')
# print(Station.All_station_list)
