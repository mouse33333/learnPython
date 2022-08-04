info = '眼界，视野；景象，风景；观点；观看'
n = 14
print (info[0:n])

import xlrd
import xlwt

workbook = xlrd.open_workbook('/users/Arthur/desktop/test.xlsx')
sheet2 = workbook.sheet_by_name('sheet1')
cols = sheet2.col_values(0)

#for x in range(0,2227):
    #file_write= open('/users/Arthur/desktop/test.txt','a')
    #file_write.write(cols[x][0:14]+'\r')
    #file_write.close()

f = xlwt.Workbook()
worksheet = f.add_sheet('my sheet')

for i in range(0, len(cols)):
    worksheet.write(0,i,label = cols[i][0:14])

f.save('/users/Arthur/desktop/demo.xls')