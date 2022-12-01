class Apputils:
    pass
@staticmethod
def check_str_is_correct(value:str)->bool:
        return not value.isspace() and not value.isdigit()
@staticmethod
def check_book_is_vaiable(value:str)->bool:
    if value=="avaiable":
        return True
