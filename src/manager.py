from src.event_couple import *
from src.event_infinite import *
import logging
from src import log
class Manager:
    def __init__(self, account, main_window, couple_list):
        self.account = account
        self.main_window = main_window
        self.couple_event = list()
        self.infinite_event = None
        if couple_list is not None:
            self.init_eventcouple(couple_list)

    def init_eventcouple(self, couple_list):
        for idx, couple_coin in enumerate(couple_list):
            primary, chain, cohesion = couple_coin[0], couple_coin[1], couple_coin[2]
            self.couple_event.insert(idx, EventCouple(idx, self.account, self.main_window, primary, chain, cohesion))

    def do_start(self, selected_id: list, trade):  # trade : method for algorithm ( ex> couple, infinite )
        if trade == 'couple':
            for idx in selected_id:
                self.couple_event[idx].start()
        elif trade == 'infinite':
            self.infinite_event = EventInfinite(0, self.account, self.main_window.coin_combobox.currentText())
            self.infinite_event.start()

    def do_stop(self, selected_id: list, trade):
        if trade == 'couple':
            for idx in selected_id:
                self.couple_event[idx].close_thread()
        elif trade == 'infinite':
            self.infinite_event.close()
            pass