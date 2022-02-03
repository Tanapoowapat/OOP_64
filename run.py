class Author:
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.name = new_name
        else:
            return "error"

author_1 = Author("bob")
print(author_1.name)
author_1 = "jerry"
print(author_1)
author_1 = "james"
print(author_1)