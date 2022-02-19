from Rent_and_Purchase import HouseRental , HousePurchase , ApartmentPurchase , ApartmentRent
class Agent:

    def __init__(self, name):
        self.name = name
        self.property_list = []
        
    def list_property(self, type_show):
        
        if type_show == True:
            for i in self.property_list :
                print(i[0])
                i[1].display()
                i[2].display()

        elif type_show == False:
            for i in self.property_list :
                print(f'Property ID : {i[1].id}')
            property_number = int(input("Enter property ID : "))
            for i in self.property_list :
                if property_number == i[1].id:
                    print(i[0])
                    i[1].display()
                    i[2].display()
                    break

    type_maps = {("house", "rental"): HouseRental,
                     ("house","purchase"): HousePurchase,
                     ("apartment","rental"): ApartmentRent,
                     ("apartment","purchase"): ApartmentPurchase
        }

    def add_property(self):
        valid_data = ("house","apartment","rental","purchase")

        validate = True
        while validate == True:
            keyword_1 = input('Enter house or apartment : ')
            if keyword_1 in valid_data:
                keyword_2 = input('Enter rental or purchase : ')
                if keyword_2 in valid_data:
                    for key in Agent.type_maps.keys():
                        if (keyword_1,keyword_2) == key:
                            Value = Agent.type_maps[(keyword_1,keyword_2)]
                            self.property_list.append(Value.prompt_init())
                            validate = False
                else:
                    print("Invalid Input")
            else:
                print("Invalid Input")

        
