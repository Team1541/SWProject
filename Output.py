from openpyxl import Workbook

def Save_excel(path, list):
    file = Workbook()
    cell = file.active()
    cell.append(['Class','Specific','Quantity'])


