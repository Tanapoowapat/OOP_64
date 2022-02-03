class Catalog:

    def __init__(self):
        self.book_list = []
    
    @property
    def Catalog_item(self):
        return self.book_list

    @Catalog_item.setter
    def Catalog_item(self, add_book):
        if isinstance(add_book, list):
            self.book_list.append(add_book)
        else:
            print("Use list bro!")


    def search_book(self, search_obj):
        for i in self.book_list:
            if search_obj in i :
                print(f'Found : {i}')
                
            elif search_obj in i[1]:
                print(f'Found : {i}')
            else:
                print("Not Found!")
                break
    
    def delete_book(self, delete_obj):
         for i in self.book_list:
            if delete_obj in i:
                self.book_list.remove(i)

            

