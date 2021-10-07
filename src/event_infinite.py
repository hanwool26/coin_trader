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

    def __trading(self):
        balance = self.account.get_balance()
        price = self.coin.get_current_price()
        amount = get_buying_amount(balance, price, self.RATIO_BUY)

        while self.__running and self.buy_count < PER_BUY:
            pass

    def start(self):
        self.__running = True
        t = threading.Thread(target=self.__trading)
        t.start()



