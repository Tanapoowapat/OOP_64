from accout import Person
from constants import Address, AccoutStatus, AccoutType

class Employee(Person):
    All_Employee_list = []

    def __init__(self, name, phone, postalbranch, username, password, accoutType, accoutStatus):
        super().__init__(name, phone, accoutType, username, password, accoutStatus)
        self.postalbranch = postalbranch

    def fetch_details(self, uid):
        return super().fetch_details(uid)

    