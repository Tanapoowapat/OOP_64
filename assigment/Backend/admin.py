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
    def creaate_employee(name, phone, postalbranch, username, password, accoutType, accoutStatus):
        if len(Employee.All_Employee_list) == 0:
            Employee.All_Employee_list.append(Employee(
                name, phone, postalbranch, username, password, accoutType, accoutStatus))
        else:
            for employee in Employee.All_Employee_list:
                if employee.name == name:
                    print('Name Already Have!')
                else:
                    Employee.All_Employee_list.append(Employee(
                        name, phone, postalbranch, username, password, accoutType, accoutStatus))

    @staticmethod
    def update_employee(uid, new_status):
        for employee in Employee.All_Employee_list:
            if uid == employee.uid:
                status = Employee.get_status(employee)
                status = new_status
                print(f'Update complate')
                return True
            else:
                print("ID Not Found!")
                return False

    @staticmethod
    def create_station(id_station, name, station_address):
        if len(Station.All_station_list) == 0:
            Station.All_station_list.append(
                Station(id_station, name, station_address))
        else:
            for station in Station.All_station_list:
                if station.name == name:
                    print('Already have station')
                else:
                    Station.All_station_list.append(
                        Station(id_station, name, station_address))


admin = Admin('Tavan', '99999999', AccoutType.Admin,
              'admin', '1234', AccoutStatus.Active)
#Employee.All_Employee_list.append(Employee('jack', '12312314', '12313', 'emp01', '1234', AccoutType.Employee, AccoutStatus.Active))
# admin.update_employee(1, AccoutStatus.Out)
#
# admin.creaate_employee('John', '12312314', '12313', 'emp01',
#                        '1234', AccoutType.Employee, AccoutStatus.Active)
# print(Employee.All_Employee_list)

admin.create_station('test', 'test', 'somewhere')
admin.create_station('test', 'test', 'somewhere')
print(Station.All_station_list)
