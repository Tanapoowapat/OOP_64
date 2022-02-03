class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def Name_Author(self):
        return self.name

# Author_2 = Author("man")
# print(Author_2.Name_Author)