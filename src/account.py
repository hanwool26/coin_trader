import pyupbit

class Account():
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key

    def get_balance(self) -> int:
        self.balance_info = self.my_upbit.get_balances()[0]
        print(f"balance : {self.balance_info['balance']} 원")
        return self.balance_info['balance']

    def connect_account(self):
        try:
            self.my_upbit = pyupbit.Upbit(self.access_key, self.secret_key)
        except Exception as e:
            print(e)