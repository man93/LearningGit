from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "Sample_excel.xlsx"
ws.sheet_properties.tabColor = "1072BA"
source = wb.active
target = wb.copy_worksheet(source)
target.title = "Sample2.xlsx"
val1 = ws.cell(row=1, column=2 ,value=10)
val2 = ws.cell(row=2, column=2, value=11)
for i in range(3,101):
	for j in range(3,101):
		ws.cell(row=i, column=j, value=i)
wb.save('Sample_excel.xlsx')
