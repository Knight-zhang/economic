# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import math

data = pd.read_excel('C:\\Users\\hp\\Desktop\\CAPM.xlsx')
jtyh = np.array(data[['交通银行']])
gsyh = np.array(data[['工商银行']])
sz = np.array(data[['上证指数']])


v = jtyh.var()
sv = math.sqrt(v)

m = gsyh.var()
sm = math.sqrt(m)

szv = sz.var()
szsv = math.sqrt(szv)
print("交通银行样本方差为",v)
print("交通银行标准差为",sv)
print("工商银行样本方差为",m)
print("工商银行标准差为",sm)
print("上证指数样本方差为",szv)
print("上证指数标准差为",szsv)