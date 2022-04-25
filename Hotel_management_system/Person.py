from Constants import Accout_Status, Accout_Type, RoomStyle, RoomStatus
from Room import Room

class Accout:
    def __init__(self, id, password, status=Accout_Status.active):
        self.__id = id
        self.__password = password
        self.__status  = status

    def reset_password(self):
        pass


class Person:
    def __init__(self, name, address, email, phone, accout_type):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__accout_type = accout_type

class Guest(Person):
    def __init__(self, name, address, email, phone, accout_type=Accout_Type.member):
        super().__init__(name, address, email, phone, accout_type)
        self.__total_room_check_in = 0

    def create_booking(self):
        pass





class Receptionist(Person):
    def __init__(self, name, address, email, phone, accout_type=Accout_Type.receptionist):
        super().__init__(name, address, email, phone, accout_type)
    
    def create_booking(self):
        pass



        
class Server(Person):
    pass

    def  add_room_charge(self, name, description, ):
        pass



Guest1 = Guest('j','1','1','2')
print(Guest1)