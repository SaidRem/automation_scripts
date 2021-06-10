# Convert all Excel files into csv format.

import os
import openpyxl
import re
from pathlib import Path

def excel_to_csv(cur_dir='.'):
    pat = re.compile('.*(.xlsx)$')
    for excel_file in filter(pat.match, os.listdir(cur_dir)):
        wb = openpyxl.load_workbook(excel_file)
        for sheet_name in wb.sheetNames:
            sheet = wb[sheet_name]
# TODO: Create csv filename form excel filename and sheet title
# TODO: Create csv file obj for writing in.
# TODO: Loop over each cell in excel file
# TODO: Write all data to csv obj and save