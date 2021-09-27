import threading
import pyupbit
from src.event_couple import *

class Event():
    def __init__(self):
        self.trade_lock = threading.Condition()
        self.account = None

    def do_buy(self, ticker, amount):
        current_price = pyupbit.get_current_price(ticker)
        self.account.buy(ticker, current_price, amount)
        pass

    def do_sell(self, ticker, price, amount):
        self.account.sell(ticker, price, amount)
