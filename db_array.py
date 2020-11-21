import random
from bl_account import Account
from bl_money import Money
from db_interface import DB_interface


class ArrayDB(DB_interface):
    arr = []

    def __init__(self):
        super().__init__()

        def get_rnd(): return random.randint(100, 999)
        def get_rnd_s(): return str(get_rnd())
        self.arr.append(Account("Ivanov"+get_rnd_s(), 10001+get_rnd(), Money(1, 1000, 0), 5.0))
        self.arr.append(Account("Petrov"+get_rnd_s(), 10002+get_rnd(), Money(1, 2000, 0), 5.0))
        self.arr.append(Account("Sidorov"+get_rnd_s(), 10003+get_rnd(), Money(1, 3000, 0), 5.0))
        self.arr.append(Account("Tikhonov"+get_rnd_s(), 10004+get_rnd(), Money(1, 4000, 0), 5.0))
        self.arr.append(Account("Pavlov"+get_rnd_s(), 10005+get_rnd(), Money(1, 5000, 0), 5.0))
        self.arr.append(Account("Kirillov"+get_rnd_s(), 10006+get_rnd(), Money(1, 6000, 0), 5.0))
        self.arr.append(Account("Mikhailov"+get_rnd_s(), 10007+get_rnd(), Money(1, 7000, 0), 5.0))
        self.arr.append(Account("Semyonov"+get_rnd_s(), 10008+get_rnd(), Money(1, 8000, 0), 5.0))
        self.arr.append(Account("Fedotov"+get_rnd_s(), 10009+get_rnd(), Money(1, 9000, 0), 5.0))
        self.arr.append(Account("Paramonov"+get_rnd_s(), 10010+get_rnd(), Money(1, 10000, 0), 5.0))

    def length(self):
        return len(self.arr)

    def get_acc(self, num: int):
        return self.arr[num]

    def set_acc(self, num: int, new_acc: Account):
        self.arr[num] = new_acc

    def add_acc(self, new_acc: Account):
        self.arr.append(new_acc)

    def del_acc(self, num: int):
        return self.arr.pop(num)
