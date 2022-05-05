from os import stat
from person import *
from packages import *



admin = Admin('test', 'test', 'Jack', '08888888', 'jack@gmail', 'Active')

class Menu:

    @staticmethod
    def create_employee():
        username = input('Enter Employee Username : ')
        password = input('Enter Employee Password : ')
        name = input('Enter Employee Password : ')
        phone = input('Enter Employee Password : ')
        email = input('Enter Employee Password : ')
        postalbranch = input('Enter Employee Password : ')

        admin.create_employee()
    
    @staticmethod
    def delete_packet():
        employee = Employee.delete_customer()

    @staticmethod
    def create_customer():
        pass

    @staticmethod
    def login():
        username = input("Username : ")
        password = input("Password : ")
        
        
        


menu = Menu()
menu.delete_packet()

