import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '../data')
UI_PATH = os.path.join(os.path.dirname(__file__), '../ui')


def get_increase_rate(current_price, base_price):
    increase_rate = round(((current_price - base_price)/base_price)*100, 2)
    print(increase_rate)
    return increase_rate

def get_buying_amount(balance, price, coherence):
    amount = (balance / price) * coherence
    return round(amount,2)
