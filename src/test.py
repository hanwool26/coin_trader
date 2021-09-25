import pyupbit
from coin import *
access_key = "xEGugKzhLrLRLa2mQMwuJfIQJBYjdA8o2CoCs83x"
secret_key = "xh2EOARx60jwjZWQ0IXy0LODLqaIYgZlLxFcbyax"
print(type(access_key))
upbit = pyupbit.Upbit(access_key, secret_key)
print(upbit.get_balances())

coin = Coin('KRW-XRP')
coin.get_current_price()

