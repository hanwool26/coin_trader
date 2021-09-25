import pyupbit

class Account():
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key
        self.balance = 0

    def get_balance(self) -> int:
        balance_info = self.my_upbit.get_balances()[0]
        self.balance = (int(balance_info['balance'].split('.')[0]))
        print(f"balance : {self.balance} 원")
        return self.balance

    def connect_account(self):
        try:
            self.my_upbit = pyupbit.Upbit(self.access_key, self.secret_key)
        except Exception as e:
            print(e)