from enum import Enum

class DeliverlyType(Enum):
    Normal, EMS = 1, 2

class AccoutStatus(Enum):
    Active, Out = 1, 2

class AccoutType(Enum):
    Admin, Employee, Customer = 1, 2, 3

class PackgesStatus(Enum):
    Receive, Deliver, Sucessfully = 1, 2, 3

class WeightType(Enum):
    Big, Small = 1, 2
