from scipy import log,exp,sqrt,stats
from matplotlib import pyplot as plt 
def bs_call_matu(S,X,T,r,sigma):
    n = 1
    x = []
    y = []
    while n <= 20:
        d1 = (log(S/X)+(r+(sigma**2)/2)*T)/(sigma*sqrt(T))
        d2 = d1 - sigma*sqrt(T)
        c = S*stats.norm.cdf(d1)-X*exp(-r*T)*stats.norm.cdf(d2)
        x.append(T)
        T = T + 0.05
        n += 1
        y.append(c)
    fig = plt.figure(dpi = 64,figsize=(10,6))
    x_values = x
    y_values = y
    plt.title("c=c(T)",fontsize=24)
    plt.plot(x_values,y_values)
    plt.grid()
    plt.show()
