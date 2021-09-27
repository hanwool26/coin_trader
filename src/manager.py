from src.event_couple import *

class Manager:
    def __init__(self, account):
        self.account = account
        pass

    def do_start(self, couple_list: list, trade):  # trade : method for algorithm ( ex> couple, infinite )
        if trade == 'couple':
            for primary, chain in couple_list:
                event_c = EventCouple(self.account, primary, chain, None)
                event_c.start()
