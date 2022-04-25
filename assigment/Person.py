from Accout import Accout
from Constant import *


class Person():
    def __init__(self, username, password, status, name, phone, accoutType, postalbranch, email):
        self.__obj_accout = Accout(username, password, status)  
        self.__name = name
        self.__phone = phone
        self.__accoutType = accoutType
        self.__postalbranch  = postalbranch
        self.__email = email
      

    def __str__ (self):
        return f'AccoutDetails{self.__obj_accout}\nName : {self.__name}\nPhone Number : {self.__phone}\nAccout Type : {self.__accoutType}\nPostalBranch{self.__postalbranch}\nE-mail : {self.__email}\n'

class Employee(Person):
    pass


class Admin(Person):
    def __init__(self, username, password, name, phone, postalbranch, email, status=AccoutStatus.Active, accoutType=AccoutType.Admin):
        super().__init__(username, password, status, name, phone,accoutType , postalbranch, email)

    
jack = Admin("jack", "1243", "Jack", "|", "BKK 01", "jack@gmail.com")
print(jack)