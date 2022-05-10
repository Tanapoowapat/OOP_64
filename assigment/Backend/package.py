from record_package import Record_Package



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
    
    def fetch_details(self):
        print("Packges Details")
        print(f'Packges ID : {self.P_id}')
        print(f'Destination : {self.destination}')
        print(f'Size : {self.Size}')
        print(f'Status : {self.Status}')
        print(f'Time : {self.Time}')
       
        
        
    def save_record(self):
        return self.Record.save_record(self.P_id, self.ID_Customer, self.destination, self.Size, self.Status, self.Time)