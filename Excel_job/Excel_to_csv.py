# Convert all Excel files into csv format.

import os
import openpyxl
import re
import csv
from pathlib import Path

def excel_to_csv(path_to_dir='.'):
    os.makedirs('excel_to_pdf', exist_ok=True)
    pat = re.compile('.*(.xlsx)$')

    for excel_file in filter(pat.match, os.listdir(path_to_dir)):
        path_to_file = Path(path_to_dir, excel_file)
        wb = openpyxl.load_workbook(path_to_file)
        # Loop through every sheet in the workbook.
        for sheet_name in wb.sheetnames:
            sheet = wb[sheet_name]
            csv_filename = Path(excel_file).stem + '_' + sheet_name + '.csv'
            with open(Path('excel_to_pdf', csv_filename), 'w', newline='') as csv_file:
                csv_obj = csv.writer(csv_file)
                for row in sheet:
                    csv_obj.writerow([d.value for d in row])
