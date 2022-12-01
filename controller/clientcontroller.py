from model.client import client


class client_controller(client):
    client_list: list[client] = []
    id_counter=0

    def addnewclient(self,full_name:str, age:str, id_no:str, phone_no:str):

        if full_name.isspace() or full_name==None:
            print("invalid name value")
            return

        cli = client(full_name=full_name,age=int(age),id_no=int(id_no),phone_no=int(phone_no),id=self.id_counter)
        self.id_counter+=1
        self.client_list.append(cli)


    def print_all_client (self=None):
        for item in self.client_list:
            print(item.get_id(),"\n",item.get_full_name(),"\n",item.get_age(),"\n",item.get_id_no(),"\n",item.get_phone_no(),"\n")
