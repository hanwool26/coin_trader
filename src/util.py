import os
import pyupbit

DATA_PATH = os.path.join(os.path.dirname(__file__), '../data')
UI_PATH = os.path.join(os.path.dirname(__file__), '../ui')

def get_increase_rate(current_price, base_price):
    increase_rate = round(((current_price - base_price)/base_price)*100, 2)
    print(increase_rate)
    return increase_rate

def get_buying_amount(balance, price, coherence):
    amount = (balance / price) * coherence
    return round(amount,2)

def get_tick_unit(price):
    if price < 10:
        return 0.01
    elif price < 100:
        return 0.1
    elif price < 1000:
        return 1
    elif price < 10000:
        return 5
    elif price < 100000:
        return 10
    elif price < 500000:
        return 50
    elif price < 1000000:
        return 100
    elif price < 2000000:
        return 500
    else:
        return 1000

def get_above_tick_price(price):
    return price + get_tick_unit(price)

def get_below_tick_price(price):
    return price - get_tick_unit(price)

def get_avg_price(avg_price, price, count):
    avg_price = ((avg_price * (count-1) + price)) / count
    return round(avg_price, 2)

def get_coin_list():
    coin_list = list()
    market_info = pyupbit.fetch_market()
    for attr in market_info:
        if 'KRW' in attr['market']:
            coin_list.append(attr['korean_name'])

    return coin_list
