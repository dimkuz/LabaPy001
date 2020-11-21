from bl_money import Money


class Account:
    surname = ""
    num = 0
    sum = Money(1, 0, 0)
    percent = 0.0

    def __init__(self, init_surname: str, init_num: int, init_sum: Money, init_percent: float) -> object:
        self.surname = init_surname
        self.num = init_num
        self.sum = init_sum
        self.percent = init_percent

    def __str__(self):
        # return f"Client name: {self.surname}\nAccount number: {self.num}\nAvailable sum: {self.sum}\nDeposit percent: {self.percent}"
        return f"[{self.surname}] [{self.num}] [{self.sum}] [{self.percent}]"

    def get_surname(self):
        return self.surname

    def get_num(self):
        return self.num

    def get_sum(self):
        return self.sum

    def get_percent(self):
        return self.percent

    def set_surname(self, new_surname: str):
        self.surname = new_surname

    def set_num(self, new_acc_num: int):
        self.num = new_acc_num

    def set_sum(self, new_acc_sum: Money):
        self.sum = new_acc_sum

    def set_percent(self, new_acc_percent: float):
        self.percent = new_acc_percent

