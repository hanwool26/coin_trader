import threading
import time
import util
import pyupbit
from event import *
from coin import *

class EventCouple(Event):
    COHERENCE = { # show chain coherence
        'welldone' : 100,
        'medium': 50,
        'rare': 20,
    }
    WAIT_TIME = [180, 300, 600]
    def __init__(self, primary_ticker, chain_ticker, coherence):
        print(type(primary_ticker), primary_ticker)
        self.primary_coin = Coin(primary_ticker)
        self.chain_coin = Coin(chain_ticker)
        self.coherence = self.COHERENCE['medium']
        self.wait_time = self.WAIT_TIME[2]
        self.__running = False

    def __monitoring(self, coherence):
        print('start monitoring', self.primary_coin.get_ticker())
        base_price = self.primary_coin.get_current_price()

        while self.__running:
            current_price = self.primary_coin.get_current_price()
            if (util.get_increase_rate(current_price, base_price)) >= 0.2:
                print('Primary Coin begin to pump up, ready to buy chain coin')
                pass
            time.sleep(self.wait_time)
            base_price = self.primary_coin.get_current_price()

    def close_thread(self):
        self.__running = False

    def start(self) -> None:
        self.__running = True
        t = threading.Thread(target=self.__monitoring, args=(self.coherence, ))
        t.start()




