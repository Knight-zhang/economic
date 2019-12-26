# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
path = ('C:\\Users\\hp\\Desktop\\gongshangBS.xlsx')
file = pd.DataFrame(pd.read_excel(path))

file_name = file["涨幅"]

arr1 = np.array(file_name)
average_f = np.mean(arr1)
std_f = np.std(arr1)
print("日收益率平均值：%.4f" % average_f,"\n日收益率标准差：%.4f" % std_f)