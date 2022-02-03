class Book:
    isbn_counter = 1
    def __init__(self):
        self.isbn = Book.isbn_counter
        self.author_name = ""
        self.title = ""
        self.subject = ""
        self.dds_nubmer = 0
        self.item_list = []
        Book.isbn_counter += 1

    @property
    def get_book(self):
        return self.item_list
    
    @get_book.setter
    def get_book(self, new_book):
        if isinstance(new_book, list):
            self.author_name = new_book[0]
            self.title = new_book[1]
            self.subject = new_book[2]
            self.dds_nubmer = new_book[3]
            new_book.insert(0,self.isbn)
            self.item_list = new_book


