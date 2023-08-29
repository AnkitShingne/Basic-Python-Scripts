#! python3
# blankRowInserter.py - Inserts gap in a sheet.

import sys, openpyxl
from openpyxl import Workbook
wb = openpyxl.load_workbook(sys.argv[3])
sheet = wb.active
for i in range(int(sys.argv[1]),(int(sys.argv[2])+3)):
	sheet.insert_rows(i)
wb.save('blank.xlsx')