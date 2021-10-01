from src.event_couple import *
import logging
from src import log
class Manager:
    def __init__(self, account, couple_list):
        self.account = account
        self.couple_event = list()
        if couple_list is not None:
            self.init_eventcouple(couple_list)

    def init_eventcouple(self, couple_list):
        for idx, couple_coin in enumerate(couple_list):
            primary, chain, cohesion = couple_coin[0], couple_coin[1], couple_coin[2]
            self.couple_event.insert(idx, EventCouple(idx, self.account, primary, chain, cohesion))

    def do_start(self, selected_id: list, trade):  # trade : method for algorithm ( ex> couple, infinite )
        if trade == 'couple':
            for idx in selected_id:
                self.couple_event[idx].start()

    def do_stop(self, selected_id: list, trade):
        if trade == 'couple':
            for idx in selected_id:
                self.couple_event[idx].close_thread()