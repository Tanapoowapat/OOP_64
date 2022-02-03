from Book import Book
from Author import Author
from catalog import Catalog

Author_1 = Author("Tanapoowapat")
Author_2 = Author("Tavan")

Book_1 = Book()
Book_2 = Book()

Book_1.get_book = [[Author_1.name, Author_2.name], "Python for newbie", "Computer", 1234]
Book_2.get_book = [Author_2.name, "Python for PRO", "Computer", 9999]


#print(Book_1.get_book)

Catalog_1 = Catalog()
Catalog_1.Catalog_item = Book_1.item_list
Catalog_1.Catalog_item = Book_2.item_list


Catalog_1.search_book("บ้าบอ")
Catalog_1.delete_book(Book_2.isbn)
print("---------------------------------"*5)
print(Catalog_1.Catalog_item)
