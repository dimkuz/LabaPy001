# account database interface
class DB_interface:
    def __init__(self):
        print("db type", type(self), "initialized")

    def length(self):
        pass

    def get_acc(self, num: int):
        pass

    def set_acc(self, num: int, new_acc):
        pass

    def add_acc(self, new_acc):
        pass

    def del_acc(self, num: int):
        pass
