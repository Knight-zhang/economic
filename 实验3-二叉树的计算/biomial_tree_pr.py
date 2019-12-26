import scipy as sp
from math import*
from scipy.special import*
print("请输入下列参数：biomial_tree_pr(s,x,u,d,n)")
def biomial_tree_pr(s,x,u,d,n):
    print("各期节点上股票价格的可能值:")
    for m in sp.arange(n+1):
        for t in sp.arange(m+1):
            S_i=u**(m-t)*d**t*s
            print("%.2f"%S_i,end=" ")
        print("\n")
    print("各期期权价值的计算结果：")
    jud=input("请输入'c'(看涨期权价值)或'p'(看跌期权价值)：")
    for m in sp.arange(n+1):
        for t in sp.arange(m+1):
            f1=max(u**(m-t)*(d**t)*s-x,0)
            f2=max(x-u**(m-t)*(d**t)*s,0)
            if jud=="c":
                print("%.2f"%f1,end=" ")
            else:
                print("%.2f"%f2,end=" ")
        print("\n")
