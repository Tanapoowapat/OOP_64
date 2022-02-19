from House import House
from Apartment import Apartment
from Rental import Rental
from Purchase import Purchase

class HouseRental(House, Rental):
    @staticmethod
    def prompt_init():
        house = House.prompt_init()
        house.update(Rental.prompt_init())
        return house

class HousePurchase(House, Purchase):
    @staticmethod
    def prompt_init():
        house = House.prompt_init()
        house.update(Purchase.prompt_init())
        return house

class ApartmentRental(Apartment, Rental):
    @staticmethod
    def prompt_init():
        apartment = Apartment.prompt_init()
        apartment.update(Rental.prompt_init())
        return apartment

class ApartmentPurchase(Apartment, Purchase):
    @staticmethod
    def prompt_init():
        apartment = Apartment.prompt_init()
        apartment.update(Purchase.prompt_init())
        return apartment

