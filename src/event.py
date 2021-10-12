import threading
import pyupbit
from src.util import *
from src.event_couple import *

STATUS_HEADER = 5 # columm number
TIME_OUT = 60

class Event():
    def __init__(self):
        self.trade_lock = None
        self.account = None
        self.ui_control = None
        self.status = 'Ready' # 'Ready' , 'Monitoring', 'Bought', 'ready to sell', 'sold'
        self.ev_id = -1

    def do_buy(self, ticker, amount):
        current_price = pyupbit.get_current_price(ticker)
        ret = self.account.buy(ticker, current_price, amount) # 현재가 윗호가 매수
        return ret

    def do_sell(self, ticker, price, amount):
        ret = self.account.sell(ticker, price, amount)
        return ret

    def get_status(self):
        return self.status

    def update_status(self, status):
        self.status = status
        if self.ui_control == None:
            print('ui control is none')
        self.ui_control.item_update(self.ev_id, STATUS_HEADER, status)

