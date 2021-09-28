import threading
import time
import src.util as util
import pyupbit
from src.event import *
from src.coin import *

class EventCouple(Event):
    BUYING_AMOUNT = { # show chain coherence
        'welldone' : 1,
        'medium': 0.5,
        'rare': 0.2,
    }
    TARGET_PROFIT = {
        'welldone': 5,
        'medium' : 3,
        'rare' : 1,
    }
    def __init__(self, account, primary_ticker, chain_ticker, coherence):
        self.account = account
        self.primary_coin = Coin(primary_ticker)
        self.chain_coin = Coin(chain_ticker)
        self.coherence = self.BUYING_AMOUNT['rare']
        self.target_per = self.TARGET_PROFIT['rare']
        self.wait_time = 3 # secs
        self.__running = False

    def do_trade(self, buying_coin, buying_price, target):
        my_balance = self.account.get_balance()
        amount = util.get_buying_amount(my_balance, buying_price, self.coherence)
        # -> Exception happens when price of chain is bigger than balance.
        print(f'ready to buy (coin : {buying_coin}, price : {buying_price}, amount : {amount}')
        pass

    def __monitoring(self):
        print(f'start monitoring : {self.primary_coin.get_ticker()} - {self.chain_coin.get_ticker()}')
        primary_base_price = self.primary_coin.get_current_price()
        chain_base_price = self.chain_coin.get_current_price()

        while self.__running:
            primary_current_price = self.primary_coin.get_current_price()
            chain_current_price = self.chain_coin.get_current_price()
            if (util.get_increase_rate(primary_current_price, primary_base_price)) >= 0.05:
                print('Primary coin begins to pump up')
                if util.get_increase_rate(chain_current_price, chain_base_price) < 3:
                    print('ready to buy chain coin')
                    self.do_trade(self.chain_coin.get_ticker(), self.chain_coin.get_current_price(), self.target_per)
                else:
                    print('chain coin already has pumped up')
            time.sleep(self.wait_time)
            primary_base_price = self.primary_coin.get_current_price()
            chain_base_price = self.chain_coin.get_current_price()

    def close_thread(self):
        self.__running = False

    def start(self) -> None:
        self.__running = True
        t = threading.Thread(target=self.__monitoring, args=())
        t.start()




