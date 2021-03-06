class Money:
    rub = 0
    kop = 0
    sign = 1

    def __init__(self, init_sign: int, init_rub: int, init_kop: int) -> object:
        # sign=1     positive sum
        # sign=0     negative sum
        if init_sign == 0:
            self.sign = 0
        else:
            self.sign = init_sign // abs(init_sign)
        self.rub = int(abs(init_rub))
        self.kop = int(abs(init_kop) % 100)

    def __truediv__(self, other):
        if type(other) is Money:
            a = self.sign * (100 * self.rub + self.kop)
            b = other.sign * (100 * other.rub + other.kop)
            c = a / b
            return c
        # else?
        if type(other) is not Money:
            a = self.sign * (100 * self.rub + self.kop)
            b = float(other)
            c = int(a / b)
            if c < 0:
                sign = -1
            else:
                sign = 1
            c = abs(c)
            return Money(sign, (c // 100), c % 100)

    def __mul__(self, other):  # __mul__ и __rmul__ это одно и то же
        a = self.sign * (100 * self.rub + self.kop)
        c = other * a
        if c < 0:
            sign = -1
        else:
            sign = 1
        c = abs(c)
        return Money(sign, (c // 100), c % 100)

    def __rmul__(self, other):  # __mul__ и __rmul__ это одно и то же. как вызвать метод __mul__ ?
        a = self.sign * (100 * self.rub + self.kop)
        c = other * a
        if c < 0:
            sign = -1
        else:
            sign = 1
        c = abs(c)
        return Money(sign, (c // 100), c % 100)

    def __add__(self, other):
        if type(other) is not Money: raise Exception('error in add')
        a = self.sign * (100 * self.rub + self.kop)
        b = other.sign * (100 * other.rub + other.kop)    # происходит ерунда если sign=0
        c = a + b
        if c < 0:
            sign = -1
        else:
            sign = 1
        c = abs(c)
        return Money(sign, (c // 100), c % 100)

    def __sub__(self, other):
        if type(other) is not Money: raise Exception('error in sub')
        a = self.sign * (100 * self.rub + self.kop)
        b = other.sign * (100 * other.rub + other.kop)   # происходит ерунда если sign=0
        c = a - b
        if c < 0:
            sign = -1
        else:
            sign = 1
        c = abs(c)
        return Money(sign, (c // 100), c % 100)

    def __str__(self):
        if self.sign < 0:
            s = "-"
        else:
            s = ""
        return s + f"{self.rub},{self.kop:02d} rub"

    def __eq__(self, other):  # x == y вызывает  x.__eq__(y).
        if type(other) is not Money: raise Exception('incompatible type for comparing')
        if self.kop == self.rub == other.kop == other.rub == 0:
            return True
        else:
            return (self.sign == other.sign) & (self.rub == other.rub) & (self.kop == other.kop)

    def __ne__(self, other):  # x != y вызывает  x.__ne__(y)
        if type(other) is not Money: raise Exception('incompatible type for comparing')
        if self.kop == self.rub == other.kop == other.rub == 0:
            return False
        else:
            return not (self.sign == other.sign) & (self.rub == other.rub) & (self.kop == other.kop)

    def __gt__(self, other):  # x > y  вызывает  x.__gt__(y).
        if type(other) is not Money: raise Exception('incompatible type for comparing')
        a = self.sign * (100 * self.rub + self.kop)
        b = other.sign * (100 * other.rub + other.kop)
        return a > b

    def __ge__(self, other):  # x ≥ y  вызывает  x.__ge__(y).
        if type(other) is not Money: raise Exception('incompatible type for comparing')
        a = self.sign * (100 * self.rub + self.kop)
        b = other.sign * (100 * other.rub + other.kop)
        return a >= b

    def __lt__(self, other):  # x < y  вызывает  x.__lt__(y).
        if type(other) is not Money: raise Exception('incompatible type for comparing')
        a = self.sign * (100 * self.rub + self.kop)
        b = other.sign * (100 * other.rub + other.kop)
        return a < b

    def __le__(self, other):  # x ≤ y  вызывает  x.__le__(y).
        if type(other) is not Money: raise Exception('incompatible type for comparing')
        a = self.sign * (100 * self.rub + self.kop)
        b = other.sign * (100 * other.rub + other.kop)
        return a <= b
