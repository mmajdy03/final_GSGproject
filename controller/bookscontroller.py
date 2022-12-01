from model.books import books



class bookscontroller(books):
    books_list: list[books] = []
    id_counter = 0
    B1="available"

    def addnewbooks(self, title:str, description:str, author:str, status:str):
        if title.isspace() or title == None:
            print("invalid name value")
            return
        print(utils.check_book_is_vaiable())
        boo = books(title=title, description=description, author=author,status=status, id=self.id_counter)
        self.id_counter += 1
        self.books_list.append(boo)

    def print_all_books(self=None):
        for item in self.books_list:
            print(item.get_id(),"\n",item.get_title(),"\n", item.get_description(), "\n", item.get_author(), "\n", item.get_status(), "\n")