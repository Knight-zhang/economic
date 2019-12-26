from scipy import *
from matplotlib import pyplot as plt
def Duration_sir(c,y,f,num_beg,n):
    a=1/f
    m=0
    x1=[]
    y1=[]
    while m<20:
        C=100*c
        p=0
        s=0
        t=num_beg/365
        for i in range(n-1):
            p_i=C*(1+y)**(-t)
            p+=p_i
            s_i=(C/(1+y)**t)*t
            s+=s_i
            t+=a
        v_pr=(100+c)/(1+y)**t
        s_pr=((C+100)/(1+y)**t)*t
        p=p+v_pr
        s+=s_pr
        D=s/p
        x1.append(c)
        y1.append(D)
        c=c+0.005
        m+=1
    fig=plt.figure(dpi=64,figsize=(10,6))
    x_values=x1
    y_values=y1
    plt.title("D=D(c)",fontsize=24)
    plt.plot(x_values,y_values)
    plt.grid()
    plt.show()