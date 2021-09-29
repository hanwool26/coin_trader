import pyupbit
import time
from src.account import *
from src.config import *
from src.event_couple import *
from src.manager import *
from src.load_file import *

if __name__ == '__main__':
    config = Config()
    config.load_config()
    access_key, secret_key = config.get_api_key()
    my_account = Account(access_key, secret_key)
    my_account.connect_account()
    my_account.get_asset()

    files = LoadFile('couple_coin_list.xlsx')
    couple_list = files.get_couple_list()

    manager = Manager(my_account)
    manager.do_start(couple_list, 'couple')

