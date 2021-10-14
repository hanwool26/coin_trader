from src.event import *
from src.coin import *
from src.util import *
import logging
import threading

INTERVAL = 1 * TIME_OUT # minutes
PER_BUY = 40 # divided by 40

class EventInfinite(Event):
    def __init__(self, idx, account, main_window):
        self.ev_id = idx
        self.account = account
        self.ui_control = main_window
        coin_name = self.ui_control.coin_combobox.currentText()

        self.coin = Coin(coin_name)
        self.__running = False
        self.RATIO_BUY = 1/PER_BUY

        self.buy_count = 0
        self.avg_price = 0
        self.total_amount = 0
        pass

    def do_buy(self, price, amount):
        try:
            ret = self.account.buy(self.coin.ticker, price, amount)
            print(ret)
            uuid = ret['uuid']

            for sec in range(TIME_OUT+1):
                if self.account.order_status(uuid) == 'done':
                    self.buy_count += 1
                    self.total_amount += amount
                    self.avg_price = get_avg_price(self.avg_price, price, self.buy_count)
                    logging.getLogger('LOG').info(f'매수 성공, 진행 : {self.buy_count}')
                    return True
                time.sleep(1)

            logging.getLogger('LOG').info('매수 실패 : 체결 타임 아웃')
            return False
        except Exception as e:
            logging.getLogger('LOG').error(e)
            self.buy_count += 1
            return False

    def __trading(self):
        balance = self.account.get_balance()
        if balance <= 0:
            logging.getLogger('LOG').info('잔고 부족')
            return
        each_asset = round(balance * self.RATIO_BUY, 2)

        cur_price = self.coin.get_current_price()
        self.avg_price = cur_price = get_above_tick_price(cur_price) # 호가 위 매수
        buying_amount = get_buying_amount(each_asset, cur_price, 1)
        if self.do_buy(cur_price, buying_amount)!= True:
            self.close()
            return

        time.sleep(INTERVAL)

        while self.__running and self.buy_count < PER_BUY:
            # order sell
            self.ui_control.update_progress(PER_BUY, self.buy_count)
            self.update_profit(get_increase_rate(cur_price, self.avg_price))
            ret = self.do_sell(self.coin.ticker, price_round(self.avg_price * 1.1), self.total_amount)
            uuid = ret['uuid']
            time.sleep(INTERVAL)
            if self.account.order_status(uuid) == 'done':
                logging.getLogger('LOG').info('매도 성공')
                self.close()
                self.start()
            else:
                self.account.cancel_order(uuid)
            # order buy
                cur_price = self.coin.get_current_price()
                above_tick_price = get_above_tick_price(cur_price)
                if cur_price <= self.avg_price:
                    buying_amount = get_buying_amount(each_asset, above_tick_price, 1)
                    self.do_buy(above_tick_price, buying_amount)
                if cur_price <= self.avg_price * 1.05:
                    buying_amount = get_buying_amount(each_asset, above_tick_price, 1)
                    self.do_buy(above_tick_price, buying_amount)

            time.sleep(1)

        ret = self.do_sell(self.coin.ticker, price_round(self.avg_price * 1.03), self.total_amount) # 3% 수익 익절. 
        self.close()

    def close(self):
        logging.getLogger('LOG').info('무한 매수 종료')
        self.__running = False
        self.avg_price = self.buy_count = self.total_amount = 0
        self.ui_control.update_progress(PER_BUY, 0)

    def start(self):
        logging.getLogger('LOG').info(f'무한 매수 시작 : {self.coin.name}')
        self.__running = True
        t = threading.Thread(target=self.__trading)
        t.start()
