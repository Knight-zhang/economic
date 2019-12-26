from scipy import *
def Duration(c,y,f,num_beg,n):
    a=1/f
    c=100*c
    t=num_beg/365
    p=0
    s=0
    for i in range(n-1):
        p_i=c*(1+y)**(-t)
        p+=p_i
        s_i=(c/(1+y)**t)*t
        s+=s_i
        t+=a
    v_pr=(100+c)/(1+y)**t
    s_pr=((c+100)/(1+y)**t)*t
    p=p+v_pr
    s+=s_pr
    D=s/p
    D_fix=D/(1+y)
    D_dol=D*p
    print("久期为：D=%.4f" % D)
    print("修正久期为：D_fix=%.4f" % D_fix)
    print("美元久期为：D_dol=%.4f" % D_dol)
