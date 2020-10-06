from money import Money


class Account:
    surname = ""
    acc_num = 0
    acc_sum = Money(1, 0, 0)
    percent = 0.0

    def __init__(self, init_surname: str, ini_acc_num: int, init_acc_sum: Money, init_acc_percent: float) -> object:
        self.surname = init_surname
        self.acc_num = ini_acc_num
        self.acc_sum = init_acc_sum
        self.percent = init_acc_percent

    def __str__(self):
        return f"Client name: {self.surname}\nAccount number: {self.acc_num}\nAvailable sum: {self.acc_sum}\nDeposit percent: {self.percent}"

    def get_surname(self):
        return self.surname

    def set_surname(self, new_surname: str):
        self.surname = new_surname

    def is_enough_to_pop_money(self, amount: Money):
        return (self.acc_sum > 0) and (self.acc_sum > amount)

    def pop_money(self, amount: Money):
        self.acc_sum -= amount
        return self.acc_sum < 0

    def push_money(self, amount: Money):
        self.acc_sum += amount

    def calculate_percent(self, days: int):
        return self.acc_sum * (self.percent / 100) * (days / 365)
