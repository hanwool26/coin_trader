from src.event import *
from src.coin import *
from src.util import *
import threading

INTERVAL = 60 * TIME_OUT
PER_BUY = 40 # divided by 40

class EventInfinite(Event):
    def __init__(self, idx, account, coin_name):
        self.ev_id = idx
        self.account = account

        self.coin = Coin(coin_name)
        self.__running = False
        self.buy_count = 0
        self.RATIO_BUY = 1/PER_BUY
        self.avg_price = 0
        pass

    def do_buy(self, price, amount):
        self.account.buy(self.coin.ticker, price, amount)
        self.buy_count = self.buy_count + 1

    def __trading(self):
        balance = self.account.get_balance()
        each_asset = round(balance * self.RATIO_BUY, 2)

        cur_price = self.coin.get_current_price()
        self.avg_price = above_tick_price = cur_price + get_tick_unit(cur_price)
        buying_amount = get_buying_amount(each_asset, above_tick_price, 1)
        self.do_buy(above_tick_price, buying_amount)
        time.sleep(INTERVAL)

        while self.__running and self.buy_count < PER_BUY:
            # order sell
            pass

    def start(self):
        self.__running = True
        t = threading.Thread(target=self.__trading)
        t.start()
