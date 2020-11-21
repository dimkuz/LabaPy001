# user interface
from db_interface import *
from bl_main import *


class UI_interface():
    db: DB_interface = None

    def __init__(self, init_base: DB_interface):
        print("ui type", type(self), "initialized")
        self.db = init_base

    def show_data(self):
        pass

    def start(self):
        pass

    def show_one_row(self, n):
        pass


