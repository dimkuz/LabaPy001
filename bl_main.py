# business logic
from bl_money import Money
from bl_account import Account
from db_interface import *
from numtostr import num2text
import random


def by_words_rus(acc: Account):
    return num2text(acc.sum.rub, ((u'рубль', u'рубля', u'рублей'), 'f')) + " " \
           + num2text(acc.sum.kop, ((u'копейка', u'копейки', u'копеек'), 'f'))


def rename_owner(account_base: DB_interface, acc_num: int, new_name: str):
    acc = account_base.get_acc(acc_num)
    acc.set_surname(new_name)
    account_base.set_acc(acc_num, acc)


def pop_money(account_base: DB_interface, acc_num: int, amount: Money):
    acc = account_base.get_acc(acc_num)
    acc_sum = acc.sum - amount
    acc.set_sum(acc_sum)
    account_base.set_acc(acc_num, acc)


def push_money(account_base: DB_interface, acc_num: int, amount: Money):
    acc = account_base.get_acc(acc_num)
    acc_sum = acc.sum + amount
    acc.set_sum(acc_sum)
    account_base.set_acc(acc_num, acc)


def charge_percent(account_base: DB_interface, acc_num: int, days: int):
    acc = account_base.get_acc(acc_num)
    acc_sum = acc.sum + acc.sum * (acc.percent / 100) * (days / 365)
    acc.set_sum(acc_sum)
    account_base.set_acc(acc_num, acc)


def add_account(account_base: DB_interface, acc: Account):
    account_base.add_acc(acc)


def sum_in_dollar(account_base: DB_interface, acc_num: int):
    return account_base.get_acc(acc_num).sum / 75


def sum_in_euro(account_base: DB_interface, acc_num: int):
    return account_base.get_acc(acc_num).sum / 90


def get_uniq_acc_num():
    return 90000 + random.randint(100, 999)
