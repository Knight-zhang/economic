import statsmodels.api as sm
import pandas as pd
import statsmodels.tsa.stattools as ts

data = pd.read_excel('./train.xlsx')
S0 = data[['spot']]
F0 = data[['future']]
F0 = sm.add_constant(F0)
mod = sm.OLS(S0,F0)
res = mod.fit()
Z1= res.model.endog - res.fittedvalues
z = ts.adfuller(Z1)
print(z)