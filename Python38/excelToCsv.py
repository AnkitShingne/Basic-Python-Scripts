#! python3
# excelToCsv.py - Converts excel files into csv files.

import openpyxl, csv, re
for files in os.dir('.'):
	if not files.endswith('.xlsx'):
		continue
	wb = openpyxl.load_workbook(files)
	for sheetname in wb.get_sheet_names():
		sheet = wb.get_sheet_by_name(sheetname)
		

