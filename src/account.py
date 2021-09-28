import pyupbit

class Account():
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key
        self.balance = 0
        self.upbit = None

    def get_balance(self) -> int:
        balance_info = self.upbit.get_balances()[0]
        self.balance = (int(balance_info['balance'].split('.')[0]))
        print(f"balance : {self.balance} 원")
        return self.balance

    def buy(self, ticker, price, amount):
        if self.get_balance() < 0:
            ret = -1
            raise Exception('no enough blanace')
        else :
            ret = self.upbit.buy_limit_order(ticker, price, amount)
            print(f'success to buy {amount} of {ticker} at {price}')
        return ret

    def sell(self, ticker, price, amount):
        ret = self.upbit.sell_limit_order(ticker, price, amount)
        return ret

    def cancel_order(self, uuid):
        ret = self.upbit.cancel_order(uuid)
        return ret

    def order_status(self, uuid):
        return self.upbit.get_order(uuid)['state']

    def connect_account(self):
        try:
            self.upbit = pyupbit.Upbit(self.access_key, self.secret_key)
        except Exception as e:
            print(e)

        if self.upbit != None:
            print('Success to access my account')