import matplotlib.pyplot as plt
from math import*
def risk_neutual(S,u,d,r,T):
    a=u*S
    b=d*S
    c=(1+r*T)**T
    qu=(c-d)/(u-d)
    plt.xlim(0,10)
    plt.ylim(0,10)
    plt.title("Binary Trees",fontsize=20)
    plt.figtext(0.13,0.45,"Stock\n=%d"%S)
    plt.figtext(0.35,0.65,"Stock\n=%d"%a)
    plt.figtext(0.35,0.35,"Stock\n=%d"%b)
    plt.figtext(0.24,0.56,"p=%.2f"%qu)
    plt.figtext(0.24,0.4,"1-p=%.2f"%(1-qu))
    plt.annotate("",xytext=(1,5),xy=(3.5,6.5),arrowprops=dict(facecolor="y",headlength=3,headwidth=4,width=1))
    plt.annotate("",xytext=(1,5),xy=(3.5,3.5),arrowprops=dict(facecolor="b",headlength=3,headwidth=4,width=1))
    plt.axis("off")
    plt.show()