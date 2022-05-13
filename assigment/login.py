from Backend.admin import Admin
from Backend.constants import *
from Backend.customer import Customer
from Backend.employee import Employee
from Backend.station import Station

class Login:
    @staticmethod
    def login_admin(username, password):
        try:
            admin = Admin.get_admin(username)
            if admin.password == password:
                return True, list[admin]
        except AttributeError as e:
            return False

    @staticmethod
    def login_employee(username, password, station_id):
        try:
            station = Station.get_station(station_id)
            employee = station.get_employee(username)
            if employee.password == password:
                return True, employee
        except AttributeError as e:
                return False

    @staticmethod
    def login_customer(username, password):
        try:
            customer = Customer.get_customer(username)
            if customer.password == password:
                return True, customer
        except AttributeError as e:
                return False


print(Login.login_customer('test','1234'))
print(Login.login_admin('admin','1234'))
print(Login.login_employee('user1', '1234', 'BKK01'))

