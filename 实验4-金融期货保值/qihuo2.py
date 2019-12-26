import statsmodels.api as sm
import pandas as pd
import numpy as np
data = pd.read_excel('./test.xlsx')
data = data.diff()
data = data.dropna()
RS = data[['spot']]
RF = data[['future']]
S1 = RS.shift(periods=1).dropna()
F1 = RF.shift(periods=1).dropna()
S0 = RS.shift(periods=-1).dropna()
F0 = RS.shift(periods=-1).dropna()
X = np.column_stack((F0,F1,S1))
mod = sm.OLS(S0,X)
res = mod.fit()
print(res.summary())