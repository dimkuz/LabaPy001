import random
from bl_account import Account
from bl_money import Money
from db_interface import DB_interface


class ExampleBase(DB_interface):
    def __init__(self):
        super().__init__()
        pass

    def length(self):
        pass

    def get_acc(self, num: int):
        pass

    def set_acc(self, num: int, new_acc: Account):
        pass

    def add_acc(self, new_acc: Account):
        pass

    def del_acc(self, num: int):
        pass
