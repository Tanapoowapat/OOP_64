from Backend.constants import Address, AccoutStatus, AccoutType

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
    def accout(self):
        return self.__obj_accout

    @property
    def name(self):
        return self.__name

    @uid.setter
    def uid(self, new_id):
        self.__uid = new_id

    def login(self, username, password):
        if username == self.accout.username:
            if 


    def fetch_details(self):
            self.username = self.accout.username
            self.password = self.accout.password
            self.status = self.accout.status
            return self.uid, self.__name, self.__phone, self.username, self.password, self.__accout_type, self.status


