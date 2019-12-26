import statsmodels.api as sm
import pandas as pd
data = pd.read_excel('./train.xlsx')
data = data.diff()
data = data.dropna()
S0 = data[['spot']]
F0 = data[['future']]
F0 = sm.add_constant(F0)
mod = sm.OLS(S0,F0)
res = mod.fit()
print(res.summary())