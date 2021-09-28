import pyupbit
import time
from src.account import *
from src.config import *
from src.event_couple import *
from src.manager import *

if __name__ == '__main__':
    config = Config()
    config.load_config()
    access_key, secret_key = config.get_api_key()
    my_account = Account(access_key, secret_key)
    my_account.connect_account()
    my_account.get_balance()

    manager = Manager(my_account)
    manager.do_start([('KRW-XTZ', 'KRW-XRP'),], 'couple')
    time.sleep(10)
    manager.do_stop()

