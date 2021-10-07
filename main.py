from src.account import *
from src.config import *
from src.manager import *
from src.load_file import *
from main_window import *
import sys
from PyQt5.QtWidgets import *

# COUPLE_FILE_PATH =

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MainWindow()

    config = Config()
    config.load_config()
    access_key, secret_key = config.get_api_key()
    my_account = Account(access_key, secret_key)
    my_account.connect_account()
    my_account.get_asset()

    files = LoadFile('couple_coin_list.xlsx')
    couple_list = files.get_couple_list()

    # load coin list from file and set the list on listView
    mywindow.set_table_data(couple_list)
    manager = Manager(my_account, mywindow, couple_list)
    mywindow.set_manager_handler(manager)

    mywindow.show()
    app.exec_()

