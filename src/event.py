import threading
import pyupbit
from src.event_couple import *

class Event():
    def __init__(self):
        self.trade_lock = None
        self.account = None
        self.status = 'Ready' # 'Ready' , 'Monitoring', 'Bought', 'ready to sell', 'sold'
        self.ev_id = -1

    def do_buy(self, ticker, amount):
        current_price = pyupbit.get_current_price(ticker)
        self.account.buy(ticker, current_price, amount)
        pass

    def do_sell(self, ticker, price, amount):
        self.account.sell(ticker, price, amount)

    def get_status(self):
        return self.status
