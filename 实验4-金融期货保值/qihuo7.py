import statsmodels.api as sm
import pandas as pd
import numpy as np
data = pd.read_excel('./train.xlsx')
RS = data[['spot']]
RF = data[['future']]
RF = sm.add_constant(RF)
mod = sm.OLS(RS,RF)
res = mod.fit()
Z1 = res.model.endog - res.fittedvalues
data = data.diff().dropna()
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
    for i in range(0,x+1):
        a.append(createVar['F'+str(i)])
    for i in range(1,x+1):
        a.append(createVar['S'+str(i)])
    return a
createVar = locals()
ass = assignment(3)
Z1 = lag(1,1,Z1)
Z1 = lag(0,3,Z1)
ass.append(Z1)
X = np.column_stack(ass)
mod = sm.OLS(S0,X)
res = mod.fit()
print (res.summary())