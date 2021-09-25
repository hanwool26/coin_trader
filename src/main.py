import pyupbit
from account import *
from config import *
from event_couple import *
if __name__ == '__main__':
    config = Config()
    config.load_config()
    access_key, secret_key = config.get_api_key()
    my_account = Account(access_key, secret_key)
    my_account.connect_account()
    my_account.get_balance()

    event_c = EventCouple('KRW-XTZ', 'KRW-XRP', None)
    event_c.start()