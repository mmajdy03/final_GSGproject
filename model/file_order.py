from model import utils
from model.books import books
from model.client import client


class order(client,books):
    def __int__(self,id:int,client_id:int,book_id:int,status:str,date:str):
        super(order, self).__init__(client_id=client.get_id(),book_id=books.get_id(),status=books.get_status())
        self.__id=id
        self.__date=date

    print(utils.check_book_is_vaiable())

    def set_date(self,date):
        self.__date = date

    def get_date(self):
        return self.__date
    def set_status(self,status):
        self.__status = status

    def get_status(self):
        return self.__status
    def set_id(self,id):
        self.__id =id

    def get_id(self):
        return self.__id
