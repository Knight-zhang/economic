import statsmodels.api as sm
import pandas as pd
import numpy as np
data = pd.read_excel('./train.xlsx')
data = data.diff()
data = data.dropna()
RS = data[['spot']]
RF = data[['future']]
def lag(x,y,z):
    if x==y:
        return z.shift(periods=x).dropna()
    else:
        return z.shift(periods=x).dropna().shift(periods=(x-y)).dropna()
def assignment(x):
    for i in range(x+1):
        createVar['S'+str(i)]=lag(i,x,RS)
    for i in range(x+1):
        createVar['F'+str(i)]=lag(i,x,RF)
    a=[]
    for i in range(x+1):
        a.append(createVar['F'+str(i)])
    for i in range(1,x+1):
        a.append(createVar['S'+str(i)])
    return a
createVar=locals()
X = np.column_stack(assignment(4))
mod = sm.OLS(S0,X)
res = mod.fit()
print(res.summary())