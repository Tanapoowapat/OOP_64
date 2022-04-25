from enum import Enum

class RoomStyle(Enum):
    standard, deluxe, famaily_Suite, business_Suite = 1, 2, 3, 4

class PaymentStatus(Enum):
    unpaid, completed, failed, cancelled, refunded = 1, 2, 3, 4, 5

class RoomStatus(Enum):
    available, occupied, notavailable = 1, 2, 3 

class BookingStatus(Enum):
    request, confimed, checkin, checkout, canceled, abandoned = 1, 2, 3, 4, 5, 6

class Accout_Status(Enum):
    active, canceled, blacklist, closed = 1, 2, 3, 4

class Accout_Type(Enum):
    member, guest, manager, receptionist = 1, 2, 3, 4


class Address:
    def __init__(self, street, sub_district, district, province, zipcode):
        self.street = street
        self.sub_district = sub_district
        self.district = district
        self.province = province
        self.zipcode = zipcode