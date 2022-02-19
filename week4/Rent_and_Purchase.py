from House import House
from Rental import Rental
from Apartment import Apartment
from Purchase import Purchase
class HouseRental(House, Rental):
    @staticmethod
    def prompt_init():
        house_init = House.prompt_init()
        Rental_init = Rental.prompt_init()
        house_rental =  "HouseRental", House(house_init["Square Feet"], house_init["Number of Bedroom"], house_init["Number of Bathroom"], house_init['Garage'], house_init['Fenced yard']), Rental(Rental_init['Furnished'], Rental_init['Rent']) 
        
        return house_rental
        
class HousePurchase(House, Purchase):
    @staticmethod
    def prompt_init():
        house_init = House.prompt_init()
        Purchase_init = Purchase.prompt_init()

        house_purchase =  "HousePurchase", House(house_init["Square Feet"], house_init["Number of Bedroom"], house_init["Number of Bathroom"], house_init['Garage'], house_init['Fenced yard']), Purchase(Purchase_init['Price']) 
        
        return house_purchase
        
class ApartmentRent(Apartment, Rental):
    @staticmethod
    def prompt_init():
        apartment_init = Apartment.prompt_init()
        Rental_init = Rental.prompt_init()
        aparent_rental =  "AparmentRental", Apartment(apartment_init["Square Feet"], apartment_init["Number of Bedroom"], apartment_init["Number of Bathroom"], apartment_init['Balcony'], apartment_init['Laundary']), Rental(Rental_init['Furnished'], Rental_init['Rent'])
        
        return aparent_rental
class ApartmentPurchase(Apartment, Purchase):
    @staticmethod
    def prompt_init():
        apartment_init = Apartment.prompt_init()
        Purchase_init = Purchase.prompt_init()

        aparent_purchase =  "AparmentPurchase", Apartment(apartment_init["Square Feet"], apartment_init["Number of Bedroom"], apartment_init["Number of Bathroom"], apartment_init['Balcony'], apartment_init['Laundary']), Purchase(Purchase_init['Price'])

        return aparent_purchase