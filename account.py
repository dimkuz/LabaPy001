from money import Money


class Account:
    surname = ""
    acc_num = 0
    acc_sum = Money(1, 0, 0)
    percent = 0.0

    def __init__(self, init_surname: str, ini_acc_num: int, init_acc_sum: Money, init_acc_percent: float):
        self.surname = init_surname
        self.acc_num = ini_acc_num
        self.acc_sum = init_acc_sum
        self.percent = init_acc_percent

    def __str__(self):
        return f"Client name: {self.surname}\nAccount number: {self.acc_num}\nAvailable sum: {self.acc_sum}\nDeposit percent: {self.percent}"

    def get_surname(self):
        pass
