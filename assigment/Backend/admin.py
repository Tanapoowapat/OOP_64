from constants import AccoutStatus, AccoutType
from employee import Employee
from accout import Person
from station import Station


class Admin(Person):
    def __init__(self, name, phone, accoutType, username, password, accoutStatus):
        super().__init__(name, phone, accoutType, username, password, accoutStatus)

    def fetch_details(self, id):
        return super().fetch_details(id)

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
                    Station.All_station_list.append(
                        Station(id_station, name, station_address))


admin = Admin('Tavan', '99999999', AccoutType.Admin,
              'admin', '1234', AccoutStatus.Active)
#Employee.All_Employee_list.append(Employee('jack', '12312314', '12313', 'emp01', '1234', AccoutType.Employee, AccoutStatus.Active))
# admin.update_employee(1, AccoutStatus.Out)

admin.create_station('test', 'test', 'somewhere')

admin.create_station('BKK01', 'Bankok', 'somewhere')

if admin.create_station('BKK01', 'Bankok', 'somewhere'):
    print('Create !')
else:
    print('Already Create')

#admin.create_employee('BKK01', 'jack', '1234', 'user1', '1234', AccoutType.Employee)



# admin.update_employee('BKK01', 2, AccoutStatus.Out)

# admin.create_employee('test')
# print(Station.All_station_list)
