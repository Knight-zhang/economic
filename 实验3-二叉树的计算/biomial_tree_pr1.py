import scipy as sp
from math import*
from scipy.special import*
print("请输入下列参数：biomial_tree_pr1(s,x,u,d,r,T,n)")
def biomial_tree_pr1(s,x,u,d,r,T,n):
    i=n+1
    for m in sp.arange(n+1):
        i-=1
        for t in sp.arange(m+1):
            S_i=u**(m-t)*d**t*s
            s1 = S_i
            sum_ft1=0
            for t in sp.arange(i+1):
                a=exp(r*T)
                p=(a-d)/(u-d)
                f1=max(u**(i-t)*(d**t)*s1-x,0)
                ft1=comb(i,t)*p**(i-t)*((1-p)**t)*f1
                sum_ft1 += ft1
            f_1=exp(-r*i*T)*sum_ft1
            print(" %.2f"%f_1,end=" ")
        print("\n")