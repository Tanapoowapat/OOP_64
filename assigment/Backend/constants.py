from enum import Enum

class AccoutStatus(Enum):
    Active, Out = 1, 2

class AccoutType(Enum):
    Admin, Employee, Customer = 1, 2, 3

class PackgesStatus(Enum):
    Receive, Deliver, Sucessfully = 1, 2, 3

class SizeType(Enum):
    Big, Small = 1, 2

class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.street_address = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country