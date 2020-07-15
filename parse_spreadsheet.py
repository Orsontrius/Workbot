import openpyxl
file = "2-15 July 2020_v3.xlsx"

def parse_spreadsheet(file):
    wb = openpyxl.load_workbook(filename=file)
    ws = wb.active

    print(ws["A"])

parse_spreadsheet(file)