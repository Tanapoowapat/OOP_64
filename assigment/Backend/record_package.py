class Record_Package():
    def __init__(self):
        self.No_transmission = 1
        self.record = []

    def show_record(self):
        for Number_info in self.record:
            print(Number_info)
        return '============================================================================================================='

    def save_record(self, P_id, ID_Customer, destination, Size, Status, Time):
        self.record.append(f'No : {self.No_transmission}    Account ID : {P_id}   ID Customer : {ID_Customer}    Destination : {destination}   Size : {Size}   Status : {Status}   Time : {Time}')
        self.No_transmission += 1