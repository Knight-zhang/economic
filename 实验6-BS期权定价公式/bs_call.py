from scipy import log,exp,sqrt,stats

def bs_call(S,X,T,r,sigma):

    d1 = (log(S/X)+(r+(sigma**2)/2)*T)/(sigma*sqrt(T))

    d2 = d1 - sigma*sqrt(T)

    c = S*stats.norm.cdf(d1)-X*exp(-r*T)*stats.norm.cdf(d2)

    print("欧式看涨期权的理论价值为：%.4f"%c)