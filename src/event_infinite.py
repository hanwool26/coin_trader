from src.event import *
import threading

INTERVAL = 5 * TIME_OUT

class EventInfinite(Event):
    def __init__(self):
        self.average_price = 0
        self.__running = False
        pass

    def __trading(self):
        while self.__running:

            pass

    def start(self):
        self.__running = True
        t = threading.Thread(target=self.__trading)
        t.start()



