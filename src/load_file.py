from openpyxl import load_workbook
import os
import logging

DATA_PATH = os.path.join(os.path.dirname(__file__), '../data')

class LoadFile:
    def __init__(self, file):
        try:
            self.load_wb = load_workbook(os.path.join(DATA_PATH, file), data_only=True)
            logging.getLogger('LOG').info(f'loading {file}')
        except Exception as e:
            logging.getLogger('LOG').error(f'failed to load {file} : {e}')

    def get_couple_list(self):
        couple_list = list()
        ws = self.load_wb.active

        for row in ws.values:
            couple_list.append(row)

        # del couple_list[0] # delete header in couple_list
        for attr in couple_list:
            print(attr)
        return couple_list

