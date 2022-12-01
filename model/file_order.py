from model.books import books
from model.client import client


class order(client,books):
    def __int__(self,client_id:int,book_id:int,status:str,date:str):
        super(order, self).__init__(client_id=client.get_id_no(),books.ge)
        self.__date=date
    def status(self,status):
        self.books.get_status()
        if status=="available":
            return true
        elif status=="unavailable":
            return false
    def set_date(self,date):
        self.__date = date

    def get_date(self):
        return self.__date
