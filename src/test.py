import pyupbit
from src.coin import *
access_key = ""
secret_key = ""
print(type(access_key))
upbit = pyupbit.Upbit(access_key, secret_key)
print(upbit.get_balances())

coin = Coin('KRW-ETH')
print(f'{coin.get_ticker()} : {coin.get_current_price()}')

