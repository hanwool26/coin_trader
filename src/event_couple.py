import threading
import time
import src.util as util
import pyupbit
from src.event import *
from src.coin import *

TIME_OUT = 60
INTERVAL = 180

class EventCouple(Event):
    BUYING_AMOUNT = { # show chain coherence
        'welldone' : 1,
        'medium': 0.5,
        'rare': 0.05,
    }
    TARGET_PROFIT = {
        'welldone': 5,
        'medium' : 3,
        'rare' : 1,
    }
    def __init__(self, account, primary_ticker, chain_ticker, coherence):
        # super
        self.account = account
        self.trade_lock = threading.Condition()

        # mine
        self.primary_coin = Coin(primary_ticker)
        self.chain_coin = Coin(chain_ticker)
        self.coherence = self.BUYING_AMOUNT['rare']
        self.target_per = self.TARGET_PROFIT['rare']
        # self.wait_time = 5 # secs

        self.__running = False

    def do_trade(self, ticker, buying_price, target):
        after_balance = my_balance = self.account.get_balance()
        amount = util.get_buying_amount(my_balance, buying_price, self.coherence)
        # -> Exception happens when price of chain is bigger than balance.
        print(f'ready to buy')
        ret = self.account.buy(ticker, buying_price, amount)
        uuid = ret['uuid']

        for sec in range(1, TIME_OUT+1):
            if sec == TIME_OUT:
                print(f'cancel order to buy {ticker}')
                self.account.cancel_order(uuid)
                return
            if self.account.order_status(uuid) == 'done':
                break
            time.sleep(1)

        print(f'bought (coin : {ticker}, price : {buying_price}, amount : {amount}')
        ret = self.selling_target(ticker, buying_price, amount, target)

    def selling_target(self, ticker, buying_price, amount, target):
        print(f'ready to sell {ticker} for {target}%')
        sell_flag = False
        while sell_flag != True:
            current_price = self.chain_coin.get_current_price()
            increase_rate =  util.get_increase_rate(current_price, buying_price)
            if increase_rate > target or increase_rate < -target:
                ret = self.account.sell(ticker, current_price, amount)
                uuid = ret['uuid']
                for sec in range(1, TIME_OUT+1):
                    if sec == TIME_OUT:
                        self.account.cancel_order(uuid)

                    if self.account.order_status(uuid) == 'done':
                        print(f'selling {ticker} with {increase_rate}%')
                        sell_flag = True
                        break
                    time.sleep(1)

        return 0 if increase_rate > 0 else -1 # selling for plus return 0, selling for minus return -1

    def __monitoring(self):
        print(f'start monitoring : {self.primary_coin.get_ticker()} - {self.chain_coin.get_ticker()}')
        primary_base_price = self.primary_coin.get_current_price()
        chain_base_price = self.chain_coin.get_current_price()

        while self.__running:
            primary_current_price = self.primary_coin.get_current_price()
            chain_current_price = self.chain_coin.get_current_price()
            if (util.get_increase_rate(primary_current_price, primary_base_price)) >= 1:
                print('Primary coin begins to pump up with 1%')
                if util.get_increase_rate(chain_current_price, chain_base_price) < 1:
                    print('ready to buy chain coin')
                    self.do_trade(self.chain_coin.get_ticker(), self.chain_coin.get_current_price(), self.target_per)
                else:
                    print('chain coin already has pumped up')
            time.sleep(INTERVAL)
            primary_base_price = self.primary_coin.get_current_price()
            chain_base_price = self.chain_coin.get_current_price()

    def close_thread(self):
        self.__running = False

    def start(self) -> None:
        self.__running = True
        t = threading.Thread(target=self.__monitoring, args=())
        t.start()




