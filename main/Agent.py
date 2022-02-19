from Rent_Purchase import HouseRental, HousePurchase, ApartmentRental, ApartmentPurchase

class Agent:

    def __init__(self):
        self.property_list = []
        self.property_list.append(Agent.add_property())

    def list_properties(self, show_all= False):
        if show_all == False:
            print('Noting to show')
        else:    
            for property in self.property_list:
                property.display()

    type_maps = {("house","rental"): HouseRental,
                    ("house","purchase"): HousePurchase,
                    ("apartment","rental"): ApartmentRental,
                    ("apartment","purchase"): ApartmentPurchase
    }

    @staticmethod
    def add_property():
        key_1 = input("Enter type of property(house/apartment) : ").lower()
        key_2 = input("Enter rental or purchase : ").lower()
        for key in Agent.type_maps.keys():
            if (key_1, key_2) == key:
                Value = Agent.type_maps[(key_1, key_2)]
                kwargs = Value.prompt_init()
        return Value(**kwargs)


while True:
    tom = Agent()
    tom.list_properties(show_all=True)
