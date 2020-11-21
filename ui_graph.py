import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from ui_graph_des import Ui_MainWindow
from ui_interface import *
#from db_interface import *
#import bl_money


class MyWin(QtWidgets.QMainWindow):
    db = None
    current_account = -1

    def __init__(self, db_init):
        QtWidgets.QWidget.__init__(self)
        self.db = db_init
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.update_table()

        self.ui.tableWidget.cellClicked.connect(self.cell_clicked)

        self.ui.buttonBox.accepted.connect(self.save_new_acc)
        self.ui.buttonBox_2.accepted.connect(self.change_owner)
        self.ui.buttonBox_3.accepted.connect(self.pop_money)
        self.ui.buttonBox_4.accepted.connect(self.push_money)
        self.ui.buttonBox_5.accepted.connect(self.charge_procent)

        self.ui.buttonBox.rejected.connect(self.reject_changes)
        self.ui.buttonBox_2.rejected.connect(self.reject_changes)
        self.ui.buttonBox_3.rejected.connect(self.reject_changes)
        self.ui.buttonBox_4.rejected.connect(self.reject_changes)
        self.ui.buttonBox_5.rejected.connect(self.reject_changes)

    def reject_changes(self):
        self.ui.lineEdit_11.clear()
        self.ui.lineEdit_12.clear()
        self.ui.lineEdit_9.clear()
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_1.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()

    def str_to_money(self,str):
        return Money(1, 0, 0)

    def save_new_acc(self):
        print("save new account")
        add_account(self.db, Account(
            self.ui.lineEdit_1.text(),
            str(get_uniq_acc_num()),
            self.str_to_money(self.ui.lineEdit_4.text()),
            float(self.ui.lineEdit_3.text()),
        ))
        self.update_table()
        self.ui.tableWidget.selectRow(self.db.length()-1)
        self.cell_clicked(self.db.length()-1)


    def change_owner(self):
        print("change owner")
        rename_owner(self.db, self.current_account, self.ui.lineEdit_6.text())
        self.update_table()

    def pop_money(self):
        print("pop money")
        try:
            rub = int(float(self.ui.lineEdit_8.text()))
            kop = int(100*float(self.ui.lineEdit_8.text())-100*rub)
            pop_money(self.db, self.current_account, Money(1, rub, kop))
        except ValueError:
            print("wrong input")
        self.update_table()

    def push_money(self):
        print("push money")
        try:
            rub = int(float(self.ui.lineEdit_10.text()))
            kop = int(100*float(self.ui.lineEdit_10.text())-100*rub)
            push_money(self.db, self.current_account, Money(1, rub, kop))
        except ValueError:
            print("wrong input")
        self.update_table()

    def charge_procent(self):
        print("charge procent")
        try:
            days = int(self.ui.lineEdit_13.text())
            charge_percent(self.db, self.current_account, days)
        except ValueError:
            print("wrong input")
        self.update_table()

    def update_table(self):
        self.ui.tableWidget.setRowCount(self.db.length())
        i = 0
        while i < self.db.length():
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(self.db.get_acc(i).get_surname())))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.db.get_acc(i).get_num())))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(self.db.get_acc(i).get_percent())))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(str(self.db.get_acc(i).get_sum())))
            i += 1

    def cell_clicked(self, row):
        self.current_account = row
        self.ui.lineEdit_11.setText(str(self.db.get_acc(row).get_surname()))
        self.ui.lineEdit_12.setText(str(self.db.get_acc(row).get_percent()))
        self.ui.lineEdit_9.setText(str(self.db.get_acc(row).get_sum()))
        self.ui.lineEdit_7.setText(str(self.db.get_acc(row).get_sum()))
        self.ui.lineEdit_5.setText(str(self.db.get_acc(row).get_surname()))
        self.ui.lineEdit_1.setText(str(self.db.get_acc(row).get_surname()))
        self.ui.lineEdit_2.setText(str(self.db.get_acc(row).get_num()))
        self.ui.lineEdit_3.setText(str(self.db.get_acc(row).get_percent()))
        self.ui.lineEdit_4.setText(str(self.db.get_acc(row).get_sum()))


class GraphUI(UI_interface):
    # db = link to database
    def __init__(self, db):
        super().__init__(db)

    def start(self):
        app = QtWidgets.QApplication(sys.argv)
        myapp = MyWin(self.db)
        myapp.show()
        sys.exit(app.exec_())
