import statsmodels.api as sm
import pandas as pd
import numpy as np
data = pd.read_excel('./train.xlsx')
data = data.diff()
data = data.dropna()
RS = data[['spot']]
RF = data[['future']]
S1 = RS.shift(periods=1).dropna().shift(periods=-1).dropna()
F1 = RF.shift(periods=1).dropna().shift(periods=-1).dropna()
S2 = RS.shift(periods=2).dropna()
F2 = RS.shift(periods=2).dropna()
S0 = RS.shift(periods=-2).dropna()
F0 = RS.shift(periods=-2).dropna()
X = np.column_stack((F0,F1,F2,S1,S2))
mod = sm.OLS(S0,X)
res = mod.fit()
print(res.summary())