from src.event import *

INTERVAL = 5 * TIME_OUT

class EventInfinite(Event):
    def __init__(self):
        self.average_price = 0
        pass

