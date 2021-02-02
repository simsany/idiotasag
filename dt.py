import itertools
import xlwt
conditions=[]
condition=input("Please enter your next condition name If you entered all of your conditions just hit enter!:")
conditions.append(condition)
while(condition):
    my_input=input("Please enter your next condition name If you entered all of your conditions just hit enter!:")
    condition = my_input  if my_input else ''
    if condition:
        conditions.append(condition)
    
condition_number=len(conditions)

cases=list(itertools.product('YN', repeat=condition_number))
workbook=book = xlwt.Workbook()
dt_sheet = book.add_sheet("DT")

for i in range(len (cases)):
    dt_sheet.write(0,i+1,f'Case{i+1}')
    
    for j in range(len(cases[i])):
        if i== 0:
            dt_sheet.write(j+1,0,conditions[j])
        dt_sheet.write(j+1,i+1,cases[i][j])

workbook.save('dt.xls')