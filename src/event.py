import threading

class Event():
    def __init__(self, account):
        self.buy_lock = threading.Condition()
        self.account = account

    def ready_buy(self, ticker):
        if self.account.get_balance() < 0:
            raise Exception('Not enough balance')
        else:
            pass
