from model.DATA import DATA


class client(DATA):
    def __init__(self,id:int, full_name: str, age: int, id_no: int, phone_no: int):
        super(client, self).__init__(self,id=id,full_name=full_name,age=age,id_no=id_no,phone_no=phone_no)
        self.__phone_no = phone_no

    def set_phone_no(self, phone_no):
        self.__phone_no = phone_no

    def get_phone_no(self):
        return self.__phone_no
