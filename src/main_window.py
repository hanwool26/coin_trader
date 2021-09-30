from PyQt5.QtWidgets import *
from PyQt5 import uic
from src.util import UI_PATH
import os
import sys

main_ui = uic.loadUiType(os.path.join(UI_PATH, 'coin_trader_main.ui'))[0]

class MainWindow(QMainWindow, main_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

