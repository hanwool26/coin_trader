import pyupbit

class Coin:
    def __init__(self, ticker):
        print(f'init coin : {ticker}')
        self.ticker = ticker
        pass

    def get_current_price(self):
        print(pyupbit.get_current_price(self.ticker))
        return pyupbit.get_current_price(self.ticker)


