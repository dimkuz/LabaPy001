import random
import math
from ui_interface import *
from db_interface import *
import os
import bl_money


class ConsoleUI(UI_interface):
    # db = link to database
    def __init__(self, db) -> object:
        super().__init__(db)

    def show_data(self):
        i = 0
        print("id : data")
        while i < self.db.length():
            print(i, ":", self.db.get_acc(i))
            i += 1

    def start(self):
        current_account = -1

        def print_menu():
            print("      = Menu =\n"
                  "      1: create new account\n"
                  "      2: rename owner\n"
                  "      3: pop money\n"
                  "      4: push money\n"
                  "      5: charge %%\n"
                  "      6: sum in dollars\n"
                  "      7: sum in euros\n"
                  "      8: sum by words (rus)\n"
                  "      #: show database\n"
                  "      !: mark current account to work with\n"
                  "      0: exit")
            if current_account < 0:
                s = "please mark account by [!] option"
            else:
                s = self.db.get_acc(current_account)
            print("working with account: " + str(s))

        def get_cmd():
            return input("enter func number: ")

        stop_signal = False
        while not stop_signal:
            print_menu()
            cmd = get_cmd()
            if cmd == "0":
                stop_signal = True
            elif cmd == "!":
                current_account = int(input("enter account id: "))
                if current_account > self.db.length():
                    print("wrong id")
                    current_account = -1
            elif cmd == "#":
                self.show_data()
#-----------------------------------------------------------------
            elif cmd == "1":  # "1: create new account\n"
                add_account(self.db, Account("new-account", 10099 + random.randint(100, 999), Money(1, 0, 0), 5.0))
                current_account = self.db.length() - 1
# -----------------------------------------------------------------
            elif cmd == "2":  # "2: rename owner\n"
                rename_owner(self.db, current_account, str(input("new name: ")))
# -----------------------------------------------------------------
            elif cmd == "3":  # "3: pop money\n"
                try:
                    rub = int(input("pop amount rub:"))
                    kop = int(input("pop amount kop:"))
                    pop_money(self.db, current_account, Money(1, rub, kop))
                except ValueError:
                    print("wrong input")
# -----------------------------------------------------------------
            elif cmd == "4":  # "4: push money\n"
                try:
                    rub = int(input("push amount rub:"))
                    kop = int(input("push amount kop:"))
                    push_money(self.db, current_account, Money(1, rub, kop))
                except ValueError:
                    print("wrong input")
# -----------------------------------------------------------------
            elif cmd == "5":  # "5: charge %%\n"
                try:
                    days = int(input("time frame in days:"))
                    charge_percent(self.db, current_account, days)
                except ValueError:
                    print("wrong input")
# -----------------------------------------------------------------
            elif cmd == "6":  # "6: sum in dollars\n"
                print(sum_in_dollar(self.db, current_account))
# -----------------------------------------------------------------
            elif cmd == "7":  # "7: sum in euros\n"
                print(sum_in_euro(self.db, current_account))
# -----------------------------------------------------------------
            elif cmd == "8":  # "8: sum by words (rus)\n"
                if current_account >= 0:
                    print(by_words_rus(self.db.get_acc(current_account)))
                else:
                    print("please mark current account")
# -----------------------------------------------------------------
            else:
                print("not realized")

            input("press enter to continue")

