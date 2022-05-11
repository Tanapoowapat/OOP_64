from Backend.admin import Admin
from Backend.employee import Employee
from Backend.station import Station

class Login:
 
 
    @staticmethod
    def login(username, password):
        for admin in Admin.All_admin_list:
            if(admin.login(username, password)):
                print('test')

    @staticmethod
    def login_customer(username, password, station_id):
        station = Station.get_station(station_id)
        for employee in station.employee_list:
            if employee.login(username, password):
                return True
            else:
                return False


        # print(station)
        # print(employee)s

Login.login('hunter00211', 'gamesinw001')
Login.login_customer('user7', '1234', 'BKK01')