from model.librarian import librarian


class librarian_controller(librarian):
    librarian_list: list[librarian] = []
    id_counter=0

    def addnewlibrarian(self,full_name:str, age:str, id_no:str, emplyment:str):
        if full_name.isspace() or full_name == None:
            print("invalid name value")
            return

        libr = librarian(full_name=full_name, age=int(age), id_no=int(id_no), emplyment=emplyment, id=self.id_counter)
        self.id_counter += 1
        self. librarian_list.append(libr)

    def print_all_librarian(self=None):
        for item in self.librarian_list:
            print(item.get_id(),"\n",item.get_full_name(), "\n", item.get_age(), "\n", item.get_id_no(), "\n", item.set_emplyment(), "\n")