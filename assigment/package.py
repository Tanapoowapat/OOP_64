class Package:
    P_id = 1
    def __init__(self, ID_Customer, destination, Size_Type, Package_Status, T):
        self.P_id = Package.P_id
        self.ID_Customer = ID_Customer
        self.destination = destination
        self.Size = Size_Type
        self.Status = Package_Status
        self.Time =  T
        self.Record = Record_Package()
        Package.P_id += 1
    
    def __str__(self):
        return f'Accout : {self.P_id} ID Customer : {self.ID_Customer} Destination : {self.destination} Size : {self.Size} Status : {self.Status} Time : {self.Time }'
        
        
    def save_record(self):
        return self.Record.save_record(self.P_id, self.ID_Customer, self.destination, self.Size, self.Status, self.Time)