import pyupbit

class Coin:
    def __init__(self, ticker):
        print(f'init coin : {ticker}')
        self.ticker = ticker
        pass

    def get_current_price(self):
        return pyupbit.get_current_price(self.ticker)

    def get_ticker(self) -> str:
        return self.ticker


