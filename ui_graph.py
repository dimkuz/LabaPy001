import sys
from PyQt5 import QtWidgets
# from PyQt5 import QtCore, QtGui, QtWidgets
from des import Ui_MainWindow
# from accbase import *


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        base = ExampleBase()
        self.ui.tableWidget.clear()
        



        # кликаем на строки, меняем поля в закладках
        self.ui.tableWidget.itemPressed.connect(self.update_fields)

        # начислить проценты
        self.ui.buttonBox_5.accepted.connect(self.handler)
        self.ui.buttonBox_5.rejected.connect(self.handler1)

        # внести деньги
        self.ui.buttonBox_4.accepted.connect(self.handler)
        self.ui.buttonBox_4.rejected.connect(self.handler1)

        # снять деньги
        self.ui.buttonBox_3.accepted.connect(self.handler)
        self.ui.buttonBox_3.rejected.connect(self.handler1)

        # сменить владельца
        self.ui.buttonBox_2.accepted.connect(self.handler)
        self.ui.buttonBox_2.rejected.connect(self.handler1)

        # открыть новый счет
        self.ui.buttonBox.accepted.connect(self.create_new_acc_accept)
        self.ui.buttonBox.rejected.connect(self.create_new_acc_reject)

    def update_fields(self):
        row = self.ui.tableWidget.currentRow()
        name = self.ui.tableWidget.item(row, 0).text()
        acc = self.ui.tableWidget.item(row, 1).text()
        proc = self.ui.tableWidget.item(row, 2).text()
        sum = self.ui.tableWidget.item(row, 3).text()
        self.ui.lineEdit_1.setText(name)
        self.ui.lineEdit_5.setText(name)
        self.ui.lineEdit_2.setText(acc)
        self.ui.lineEdit_3.setText(proc)
        self.ui.lineEdit_12.setText(proc)
        self.ui.lineEdit_4.setText(sum)
        self.ui.lineEdit_7.setText(sum)
        self.ui.lineEdit_9.setText(sum)
        self.ui.lineEdit_11.setText(sum)

    def create_new_acc_accept(self):
        self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)
        r = self.ui.tableWidget.rowCount() - 1
        self.ui.tableWidget.setItem(r, 0, QtWidgets.QTableWidgetItem(self.ui.lineEdit_1.text()))
        self.ui.tableWidget.setItem(r, 1, QtWidgets.QTableWidgetItem(self.ui.lineEdit_2.text()))
        self.ui.tableWidget.setItem(r, 2, QtWidgets.QTableWidgetItem(self.ui.lineEdit_3.text()))
        self.ui.tableWidget.setItem(r, 3, QtWidgets.QTableWidgetItem(self.ui.lineEdit_4.text()))
        self.ui.tableWidget.resizeColumnsToContents()

    def create_new_acc_reject(self):
        self.ui.lineEdit_1.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()

    def handler(self):
        pass

    def handler1(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
