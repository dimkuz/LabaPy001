from db_main import AccountBase
from bl_main import *
from account import Account
from money import Money

eb = AccountBase()

print(eb.length())

print(eb.get_acc(9))
print(is_enough_to_pop_money(eb.get_acc(9), Money(1, 10000, 0)))

# i = 0
# while i < eb.length():
#     print(eb.get_acc(i), "\n")
#     i += 1
