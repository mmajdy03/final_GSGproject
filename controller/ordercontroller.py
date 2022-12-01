from model import file_order


class order_controller:
    order_list: list[file_order] = []
    id_counter = 0

    def addneworder(self,client_id:str,book_id:str,status:str,date:str):


        cli = file_order(client_id=int(client_id), book_id=int(book_id),status=status, date=date, id=self.id_counter)
        self.id_counter += 1
        self.order_list.append(cli)

    def print_all__order(self=None):
        for item in self.order_list:
            print(item., "\n", item.get_full_name(), "\n", item.get_age(), "\n", item.get_id_no(), "\n",
                  item.get_phone_no(), "\n")
