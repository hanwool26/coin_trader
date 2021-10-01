from PyQt5.QtWidgets import *
from PyQt5 import uic
from src.util import UI_PATH
import os
import sys

# for test couple_list = [('선두코인', '후발코인'), ('이더', '비트'), ('리플', '슨트'), ('리플', '스텔라')]

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(os.path.join(UI_PATH, 'main.ui'), self)

        self.manager_handler = None
        self.sel_id = list()
        self.trade = 'couple'

        self.list_view = self.findChild(QTableWidget, 'list_view')
        self.list_view.cellClicked.connect(self.cellclicked_event)

        self.trade_btn = self.findChild(QPushButton, 'trade_btn')
        self.trade_btn.clicked.connect(self.trade_btn_event)

        self.stop_btn = self.findChild(QPushButton, 'stop_btn')
        self.stop_btn.clicked.connect(self.stop_btn_event)

        self.asset_info = self.findChild(QLineEdit, 'asset_info')

    def set_table_data(self, couple_list):
        header = couple_list[0]
        self.list_view.setColumnCount(len(header))
        self.list_view.setHorizontalHeaderLabels(header)
        del couple_list[0]
        num_of_list = len(couple_list)
        self.list_view.setRowCount(num_of_list)

        for rownum, row in enumerate(couple_list):
            for col, val in enumerate(row):
                item = QTableWidgetItem(val)
                self.list_view.setItem(rownum,col, item)

    def cellclicked_event(self, row,col):
        selected = self.list_view.selectedIndexes()
        self.sel_id = [idx.row() for idx in selected]

    def trade_btn_event(self):
        print('trade start')
        self.manager_handler.do_start(self.sel_id, self.trade)

    def stop_btn_event(self):
        print('stop trade')
        self.manager_handler.do_stop(self.sel_id, self.trade)

    def set_manager_handler(self, manager):
        self.manager_handler = manager
        self.show_asset_info()

    def show_asset_info(self):
        asset_str = f'자산 : {self.manager_handler.account.get_asset()} 원'
        self.asset_info.setText(asset_str)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.set_table_data(couple_list)
    mywindow.show()
    app.exec_()
