# -*- coding: utf-8 -*-
import statsmodels.api as sm
import numpy as np

b = [(0.9,0.5),(0.6,0.4),(0.2,0.8)]
r = [0.15,0.12,0.18]  

b = np.array(b)
r = np.array(r)

b = sm.add_constant(b)

mod = sm.OLS(r,b)
res = mod.fit()
print(res.summary())

