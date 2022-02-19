from House import House
from Rental import Rental
from Apartment import Apartment
from Purchase import Purchase

class HouseRental(House, Rental):
    @staticmethod
    def prompt_init():
        house_init = House.prompt_init()
        Rental_init = Rental.prompt_init()
        house_rental =  "HouseRental", House(house_init["Square Feet"], house_init["Square Feet"], house_init["Number of Bedroom"], house_init['Garage'], house_init['Fenced yard']), Rental(Rental_init['Furnished'], Rental_init['Rent']) 
        return house_rental

        

class HousePurchase(House, Purchase):
    @staticmethod
    def prompt_init():
        house_init = House.prompt_init()
        house_init.update(Purchase.prompt_init())

        house_purchase =  "HouseRental", House(house_init["Square Feet"], house_init["Square Feet"], house_init["Number of Bedroom"], house_init['Garage'], house_init['Fenced yard']), Rental(Rental_init['Furnished'], Rental_init['Rent']) 
        return type_rental
        
class ApartmentRent(Apartment, Rental):
    @staticmethod
    def prompt_init():
        aparent_init = Apartment.prompt_init()
        aparent_init.update(Rental.prompt_init())
        
        return aparent_init


class ApartmentPurchase(Apartment, Purchase):
    @staticmethod
    def prompt_init():
        apartment_init = Apartment.prompt_init()
        apartment_init.update(Purchase.prompt_init())
        return apartment_init