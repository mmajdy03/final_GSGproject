from model.DATA import DATA


class librarian(DATA):
    def __init__(self,id:int, full_name:str, age:int, id_no:int, emplyment:str):
        super(librarian, self).__init__(self,id=id, full_name=full_name, age=age, id_no=id_no)
        self.__emplyment = emplyment

    def set_emplyment(self, emplyment):
        self.__emplyment = emplyment

    def get_phone_no(self):
        return self.__emplyment
