import pandas as pd
import statsmodels.tsa.stattools as ts

data = pd.read_excel('./train.xlsx')
sp = data['spot']
fu = data['future']
s = ts.adfuller(sp,1)
f = ts.adfuller(fu,1)
print(s,f)