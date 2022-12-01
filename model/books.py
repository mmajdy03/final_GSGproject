from model.DATA import DATA


class books(DATA):
    def __int__(self,id:int,title:str,description:str,author:str,status:str):
        self.__id=id
        self.__title=title
        self.__description =description
        self.__author =author
        self.__status =status

    def set_id(self,id):
        self.__id = id

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title
    def set_title(self, title):
        self.__title = title
    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author
    def set_description(self, description):
        self.__description = description
    def get_description(self):
        return self.__description

    def set_status(self, status):
        self.__status=status

    def get_status(self):
        return self.__status
