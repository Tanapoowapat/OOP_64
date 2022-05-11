from constants import Address, AccoutStatus, AccoutType

class Accout:

    def __init__(self, username, password, accoutStatus):
        self.__username = username
        self.__password = password
        self.__accout_status = accoutStatus

    @property
    def password(self):
        return self.__password

    @property
    def username(self):
        return self.__username

    @property
    def status(self):
        return self.__accout_status

    @status.setter
    def status(self, new_status):
        self.__accout_status = new_status

    def __str__(self):
        return f'Username: {self.__username}\nPassword: {self.password}\nStatus: {self.__accout_status}'

class Person():
    Auto_id = 1
    def __init__(self, name, phone, accoutType, username, password, accoutStatus):
        self.__uid = Person.Auto_id
        self.__name = name
        self.__phone = phone
        self.__accout_type = accoutType
        self.__obj_accout = Accout(username, password, accoutStatus)
        Person.Auto_id += 1

    @property
    def status(self):
        status = self.__obj_accout.status 
        return status

    @status.setter
    def status (self, new_status):
        self.__obj_accout.status = new_status

    @property
    def uid(self):
        return self.__uid

    @property
    def name(self):
        return self.__name

    @uid.setter
    def uid(self, new_id):
        self.__uid = new_id

    def fetch_details(self, uid):
        if uid == self.uid:
            print(f'ID : {self.uid}')
            print(f'Name : {self.__name}')
            print(f'Phone : {self.__phone}')
            print(f'Accout Type : {self.__accout_type}')
            print(f'=====Accout Details=====')
            print(f'{self.__obj_accout}')
        else:
            print("ID NotFound!")


