from datetime import datetime
from Constants import *

class Search:
    def search(self, style, start_date, duration):
        pass



class Room(Search):
    def __init__(self, room_number, room_style, status, price, is_smoking):
        self.__room_number = room_number
        self.__style = room_style
        self.__status = status
        self.__booking_price = price
        self.__is_smoking = is_smoking

        self.__keys = []
        self.__house_keeping_log = []

    def is_room_available(self):
        pass

    def check_in(self):
        pass

    def check_out(self):
        pass

    def search(self, style, start_date, duration):
        pass
    

class RoomKey:
    def __init__(self, key_id, barcode, is_active, is_master):
        self.__key_id = key_id
        self.__barcpde = barcode
        self.__issue_at = datetime.date.today()
        self.active = is_active
        self.__is_master = is_master

    def assign_room(self, room):
        pass

    def is_active(self):
        pass


class RoomHouseKeeping:
    def __init__(self, desciption, duration, house_keeper):
        self.__description = desciption
        self.__start_datetime = datetime.date.today()
        self.__duration = duration  
        self.__house_keeper = house_keeper

    def add_house_keeper(self, room):
        pass