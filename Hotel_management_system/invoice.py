class InvoiceItem:
    def __init__(self, amount):
        self.amount = amount

    def updateAmount(self):
        pass

class Amenity(InvoiceItem):
    def __init__(self, name, description,amount):
        super().__init__(amount)
        self.name = name


class RoomService(InvoiceItem):
    def __init__(self, is_chargeable, request_time):
        super().__init__(amount)
        self.is_chargeable = is_chargeable
        self.request_time = request_time


class KitchenService(InvoiceItem):
    def __init__(self, description, amount):
        super().__init__(amount)
        self.__description = description