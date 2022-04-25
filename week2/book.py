class Catalog:
    def __init__(self):
        self.book_list = []

    def add_catalog(self, book):
        for i in book:
            self.book_list.append(i)

    def search_book(self, search_obj):
        self.show_book_list = []
        for i in self.book_list:
            if str(search_obj) in i:
                self.show_book_list.append(i)
            elif str(search_obj) in i[1]:
                self.show_book_list.append(i)

        if len(self.show_book_list) == 0:
            return f"{search_obj} not found in book list"
        return self.show_book_list

    def delete_book(self, delete_obj):

        h = 0
        for i in self.book_list:
            if str(delete_obj) in i:
                self.book_list.pop(h)
            elif str(delete_obj) in i[1]:
                self.book_list.pop(h)
            h += 1

        return self.book_list


class Book:

    def __init__(self, isbn, author_name, title, subject, dds_number):
        self.isbn = isbn
        self.author_name = author_name
        self.title = title
        self.dds_nubmer = dds_number
        self.subject = subject
        self.book = []
        self.book.append([str(self.isbn), self.author_name, self.title, self.subject, str(self.dds_nubmer)])



class Author:
    def __init__(self, name):
        self.name = name


Author_1 = Author("Tanapoowapat")
Author_2 = Author("Tavan")

Book_1 = Book(1, [Author_1.name, Author_2.name], "Python for newbie", "Computer", 1234)
Book_2 = Book(2, Author_2.name, "Python for PRO", "Computer", 9999)
Book_3 = Book(3, Author_2.name,"Python for PRO V2", "Computer", 9999)

Catalog = Catalog()

Catalog.add_catalog(Book_1)
Catalog.add_catalog(Book_2)
Catalog.add_catalog(Book_3)

# print(Catalog.search_book("Tanapoowapat"))


#Catalog.delete_book(Book_1.)
print(Catalog.book_list)