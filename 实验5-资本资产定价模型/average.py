# -*- coding: utf-8 -*-
import xlrd
file_name = 'C:\\Users\\hp\\Desktop\\CAPM.xlsx'
xls = xlrd.open_workbook(filename=file_name)

sheet = xls.sheets()[0]

jtyh = sheet.col_values(1)
del jtyh[0]
sum = 0
for each in jtyh:
    sum+= each
ave = sum/(len(jtyh))
print("交通银行")
print(ave)

gsyh = sheet.col_values(2)
del gsyh[0]
sum = 0
for each in gsyh:
    sum += each
ave = sum/(len(gsyh))
print("工商银行")
print(ave)

sz = sheet.col_values(3)
del sz[0]
sum = 0
for each in sz:
    sum += each
ave = sum/(len(sz))
print("上证指数")
print(ave)

