from src.event_couple import *

class Manager:
    def __init__(self, account):
        self.account = account
        self.event = list()
        pass

    def do_start(self, couple_list: list, trade):  # trade : method for algorithm ( ex> couple, infinite )
        if trade == 'couple':
            for idx, couple_coin in enumerate(couple_list):
                primary, chain, cohesion = couple_coin[0], couple_coin[1], couple_coin[2]
                self.event.insert(idx, EventCouple(idx, self.account, primary, chain, cohesion))
                self.event[idx].start()

    def do_stop(self):
        for idx in range(len(self.event)):
            self.event[idx].__running = False