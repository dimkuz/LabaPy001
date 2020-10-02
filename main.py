from money import Money
from account import Account

acc1 = Account("Smirnoff",
               1000,
               Money(1, 1000, 0),
               5.0)
print(acc1)
