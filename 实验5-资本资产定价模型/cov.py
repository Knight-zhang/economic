# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

data = pd.read_excel('C:\\Users\\hp\\Desktop\\CAPM.xlsx')
jtyh = np.array(data['交通银行'])
shang = np.array(data['上证指数'])
gsyh = np.array(data['工商银行'])
 
c = np.cov(jtyh,shang)  
c1 = np.cov(gsyh,shang)
print(c)
print(c1)