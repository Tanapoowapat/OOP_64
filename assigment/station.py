class Station:
    station_auto_id = 1

    def __init__(self, name): 
        self.__station_id = Station.station_auto_id
        self.__name = name
        Station.station_auto_id += 1

    def __str__(self):
        return f"Station ID : {self.__station_id}\nStation name: {self.__name}"

    @staticmethod
    def create_employee():
        pass

    @staticmethod
    def show_employee():
        pass

class All_station():
    all_station_list = []
    
    @staticmethod
    def create_station(name):
        station = ()

    def show_station():
        pass