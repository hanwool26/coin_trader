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
        try:
            ret = self.account.sell(ticker, price, amount)
            print(f'do sell : {ticker}, {price}, {amount}')
        except Exception as e:
            print(e)
        return ret

    def get_status(self):
        return self.status

    def update_info(self, price, avg_price, amount, profit_rate):
        info = f'현재가: {price} | 평단가: {avg_price} | 평가손익 : {round(((avg_price*amount) * profit_rate)/100, 2)} | 수익률 : {profit_rate} %'
        if self.ui_control == None:
            print('ui control is none')
        else:
            self.ui_control.update_info(info)

    def update_status(self, status):
        self.status = status
        if self.ui_control == None:
            print('ui control is none')
        else:
            self.ui_control.item_update(self.ev_id, STATUS_HEADER, status)

    def update_progress(self, max, count):
        if self.ui_control == None:
            print('ui control is none')
        else:
            self.ui_control.update_progress(max, count)


