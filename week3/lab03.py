class Note:
    note_id_counter = 1

    def __init__(self, Memo, tag, date):
        self.id = Note.note_id_counter
        self.Memo = Memo
        self.tag = tag
        self.date = date
        Note.note_id_counter += 1

    def __str__(self):
        return f'Note ID : {self.id} Memo : {self.Memo} Tags : {self.tag} Date : {self.date}'

    def match_note(self, search_filter):
        list_match = [self.id, self.Memo, self.tag]
        if isinstance(self.date, list):
            for i in self.date:
                list_match.append(i)
        else:
            list_match.append(self.date)
        if search_filter in list_match:
            return True
        else:
            return False


class NoteBook:
    def __init__(self):
        self.list_note = []

    def new_note(self, Note):
        self.list_note.append(Note)

    def search_note(self, search_filter):
        for i in self.list_note:
            if isinstance(search_filter, list):
                list_filter = []
                for tags in search_filter:
                    if i.match_note(tags) == True:
                        if i not in list_filter:
                            list_filter.append(i)
                if len(list_filter) > 0:
                    for i in list_filter:
                        print(i)

            elif isinstance(search_filter, str):
                if i.match_note(search_filter) == True:
                    print(i)

    def modify_memo(self, note_id, memo, type=None):
        for i in self.list_note:
            if note_id == str(i.id):
                i.Memo = memo

    def modify_tags(self, note_id, tags, type=None):
        for i in self.list_note:
            if note_id == str(i.id):
                i.tag = tags


class Menu:
    
    @staticmethod
    def show_note():
        for i in NoteBook.list_note:
            print(i)

    @staticmethod
    def search_note():
        search_word = str(input(f"What do you want to find : "))
        NoteBook.search_note(search_word)

    @staticmethod
    def new_note(Note):
        NoteBook.new_note(Note)

    @staticmethod
    def modify_memo():
        Menu.show_note()
        id_memo = str(input("Select note id to modify : "))
        memo_modify = str(input("New memo : "))
        NoteBook.modify_memo(id_memo, memo_modify)

    @staticmethod
    def modify_tags():
        Menu.show_note()
        id_tags = str(input("Select note id to modify : "))
        tags_modify = str(input("New tags : "))
        NoteBook.modify_tags(id_tags, tags_modify)


NoteBook = NoteBook()
menu = Menu()

run = True

while run:
    paper_note = []
    print('='*30)
    print('Menu')
    print('='*30)
    print('1 : Create note \n2 : Search note \n3 : Modify note\n4 : Show note\n5 : Exit')
    print('='*30)
    Command_Option = int(input('Select : '))

    if Command_Option == 1:
        Memo = str(input(f"Note Memo :"))
        tag = str(input(f'Tag : '))
        date = str(input(f'Date[day/month/year] : '))
        I_note = Note(Memo, tag, date)
        Menu.new_note(I_note)

    elif Command_Option == 2:
        if len(NoteBook.list_note) == 0:
            print('=' * 30)
            print('Notebook is Empty')
        else:
            print('=' * 30)
            Menu.search_note()

    elif Command_Option == 3:
        if len(NoteBook.list_note) == 0:
            print('=' * 30)
            print('Notebook is Empty')
        else:
            print('='*30)
            print('Modify Menu')
            print('=' * 30)
            select = int(input(f"1. for modify Memo \n2. for modify tags \nSelect Option: "))
            print('=' * 30)
            if select == 1:
                Menu.modify_memo()
            elif select == 2:
                Menu.modify_tags()
            else:
                print('=' * 30)
                print('Invalid Input')

    elif Command_Option == 4:
        if len(NoteBook.list_note) == 0:
            print('='*30)
            print('Notebook is Empty')
        else:
            print('=============Note=============')
            Menu.show_note()

    elif Command_Option == 5:
        run = False
    else:
        print('Invalid input')