from Rent_and_Purchase import HouseRental , HousePurchase , ApartmentPurchase , ApartmentRent


class Agent:

    def __init__(self, name):
        self.name = name
        self.property_list = []
        
    def list_property(self, type_show):
        
        if type_show == True:
            for i in self.property_list :
                i[1].display()
                i[2].display()

        elif type_show == False:
            for i in self.property_list :
                print(f'property No. {i[1].id}')
            property_number = int(input("Enter property Number : "))
            for i in self.property_list :
                if property_number == i[1].id:
                    i[1].display()
                    i[2].display()

    type_maps = {("house", "rental"): HouseRental,
                     ("house","purchase"): HousePurchase,
                     ("apartment","rental"): ApartmentRent,
                     ("apartment","purchase"): ApartmentPurchase
         }   

    def add_property(self):
        keyword_1 = input('Enter house or apartment : ')
        keyword_2 = input('Enter rental or purchase : ')
        for key in Agent.type_maps.keys():
            if (keyword_1,keyword_2) == key:
                Value = Agent.type_maps[(keyword_1,keyword_2)]
                self.property_list.append(Value.prompt_init())
        

        
