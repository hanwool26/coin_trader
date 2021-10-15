from PyQt5.QtWidgets import *
from PyQt5 import uic
from src.util import UI_PATH, util_strip
from src import log
import os
import sys
import logging

HEADER_SUFFIX = ('진행상태', )
# for test couple_list = [('선두코인', '후발코인'), ('이더', '비트'), ('리플', '슨트'), ('리플', '스텔라')]

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        if getattr(sys, 'frozen', False):
            res_path = os.path.realpath(sys.executable)
        elif __file__:
            res_path = os.path.realpath(__file__)
        uic.loadUi(res_path[:res_path.rfind('\\')] + '\\\\ui\\main.ui', self)

        self.manager_handler = None
        self.sel_id = list()
        self.trade = 'infinite'
        self.invest_asset = 0

        self.list_view = self.findChild(QTableWidget, 'list_view')
        self.list_view.cellClicked.connect(self.cellclicked_event)

        self.trade_btn = self.findChild(QPushButton, 'trade_btn')
        self.trade_btn.clicked.connect(self.trade_btn_event)

        self.stop_btn = self.findChild(QPushButton, 'stop_btn')
        self.stop_btn.clicked.connect(self.stop_btn_event)

        self.asset_info = self.findChild(QLineEdit, 'asset_info')
        self.profit_info = self.findChild(QLineEdit, 'profit_lineEdit')

        self.invest_asset_lineedit = self.findChild(QLineEdit, 'invest_asset_lineEdit')

        # group box
        self.couple_r_btn = self.findChild(QRadioButton, 'couple_r_btn')
        self.couple_r_btn.clicked.connect(self.radio_btn_event)
        self.infinite_r_btn = self.findChild(QRadioButton, 'infinite_r_btn')
        self.infinite_r_btn.clicked.connect(self.radio_btn_event)

        # coin list combo box
        self.coin_combobox = self.findChild(QComboBox, 'coin_comboBox')
        self.interval_combobox = self.findChild(QComboBox, 'interval_comboBox')
        self.asset_rate_combobox = self.findChild(QComboBox, 'asset_rate_comboBox')
        self.asset_rate_combobox.currentIndexChanged.connect(self.handler_asset_rate_combobox)

        self.progressbar = self.findChild(QProgressBar, 'progressBar')
        self.progressbar.setValue(0)

        self.log_view = self.findChild(QTextBrowser, 'log_view')
        self.log_handler = log.QTextEditLogger(self.log_view)
        self.log_handler.setFormatter(logging.Formatter('[%(asctime)s] %(message)s'))
        logging.getLogger('LOG').addHandler(self.log_handler)
        logging.getLogger('LOG').setLevel(logging.DEBUG)

    def update_info(self, info):
        self.profit_info.setText(info)

    def update_progress(self, max, count):
        var = 100 / max
        self.progressbar.setValue(var * count)

    def set_table_data(self, couple_list):
        header = couple_list[0] + HEADER_SUFFIX
        self.list_view.setColumnCount(len(header))
        self.list_view.setHorizontalHeaderLabels(header)
        del couple_list[0]
        num_of_list = len(couple_list)
        self.list_view.setRowCount(num_of_list)

        for rownum, row in enumerate(couple_list):
            for col, val in enumerate(row):
                self.item_update(rownum, col, val)

    def set_asset_rate_combobox(self):
        asset_rates = [10, 25, 50, 100]
        for rate in asset_rates:
            self.asset_rate_combobox.addItem(f'{str(rate)} %')
        self.asset_rate_combobox.setCurrentText('자산 비율')

    def handler_asset_rate_combobox(self):
        self.invest_asset = self.manager_handler.account.get_balance() * (util_strip(self.asset_rate_combobox.currentText()) / 100)
        self.invest_asset_lineedit.setText(f'투자금액 : {(round(self.invest_asset, 2))} 원')

    def set_coin_combobox(self, coin_list):
        if coin_list == None:
            return
        for coin in coin_list:
            self.coin_combobox.addItem(coin)

    def set_interval_combobox(self):
        interval = [1,3,6,9,12,24]
        for time in interval:
            self.interval_combobox.addItem(str(time))
        self.interval_combobox.setCurrentText('Interval')

    def item_update(self, row, col, val):
        item = QTableWidgetItem(val)
        if item != None:
            self.list_view.setItem(row,col,item)

    def cellclicked_event(self, row, col):
        selected = self.list_view.selectedIndexes()
        self.sel_id = [idx.row() for idx in selected]

    def trade_btn_event(self):
        self.manager_handler.do_start(self.sel_id, self.trade)

    def stop_btn_event(self):
        self.manager_handler.do_stop(self.sel_id, self.trade)

    def radio_btn_event(self):
        if self.couple_r_btn.isChecked():
            self.trade = 'couple'
        elif self.infinite_r_btn.isChecked():
            self.trade = 'infinite'

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
