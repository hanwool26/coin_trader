import threading
import time
from coin import *

class EventCouple():
    COHERENCE = {
        'welldone' : 100,
        'medium': 50,
        'rare': 20,
    }
    WAIT_TIME = [60, 180, 300]
    def __init__(self, primary_ticker, chain_ticker, coherence):
        self.primary_coin = Coin(primary_ticker)
        self.chain_coin = Coin(chain_ticker)
        self.coherence = self.COHERENCE['medium']
        self.wait_time = self.WAIT_TIME[2]
        self.__running = False

    def __monitoring(self, coherence):
        print('start monitoring')
        current_price = self.primary_coin.get_current_price()
        base_price = current_price

        print('in while')
        while self.__running:
            print(current_price)
            if ((current_price - base_price)//base_price)*100 >= 10:
                print('Primary Coin begin to pump up, ready to buy chain coin')
                pass
            time.sleep(self.wait_time)
            current_price = self.primary_coin.get_current_price()

    def start(self) -> None:
        self.__running = True
        t = threading.Thread(target=self.__monitoring, args=(self.coherence, ))
        t.daemon = True
        t.start()




