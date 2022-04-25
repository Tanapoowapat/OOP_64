class Accout():
    
    id_counter = 1

    def __init__(self, username, password, status):
        self.__id = Accout.id_counter
        self.__username = username
        self.__password = password
        self.__status = status
        Accout.id_counter += 1

    def __str__(self):
        return f'Accout ID : {self.__id}\nAccout Username : {self.__username}\nAccout Passowrd : {self.__password}\nAccout Status : {self.__status}'
