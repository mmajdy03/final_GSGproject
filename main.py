from controller.clientcontroller import client_controller
from controller.librariancontroller import librarian_controller
from controller.bookscontroller import bookscontroller
from controller.ordercontroller import order_controller
cli_controller= client_controller()
libr_cntroller = librarian_controller()
book_controller= bookscontroller()
order_controller= order_controller()
def get_clint_inputs():
    full_name = input("Enter the full name :")
    age = input("Enter the age :")
    id_no = input("Enter the id_no :")
    phone_no = input("Enter the phone_no :")
    cli_controller.addnewclient(full_name=full_name, age=age, id_no=id_no, phone_no=phone_no)


def get_librarian_inputs():
    full_name = input("Enter the full name :")
    age = input("Enter the full name :")
    id_no = input("Enter the full name :")
    emplyment = input("Enter the employment :")
    libr_cntroller.addnewlibrarian(full_name=full_name, age=age, id_no=id_no, emplyment=emplyment)
def get_order_inputs():
    client_id= input("Enter the  client_id :")
    book_id = input("Enter the  book_id :")
    status = input("Enter the status :")
    date = input("Enter the full name :")

    order_controller.addneworder(client_id=client_id, book_id=book_id, status=status, date= date)



A1 = input("Enter the profile number to be registered\n"
           "1_client"
           "2_liabrarian")
A1 = int(A1)
if A1 == 1:
    get_clint_inputs()

elif A1 == 2:
    get_librarian_inputs()
    get_order_inputs()
    print(utils.check_book_is_vaiable)
else:
    print("the input number is error")
cli_controller.print_all_client()
libr_cntroller.print_librarian()
book_controller.print_all_books()