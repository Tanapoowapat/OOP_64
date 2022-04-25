from enum import Enum

class AccoutStatus(Enum):
    Active, Canceld = 1, 2

class AccoutType(Enum):
    Admin, Employee = 1, 2

class PackgesStatus(Enum):
    Receive, Deliver, Sucessfully = 1, 2, 3