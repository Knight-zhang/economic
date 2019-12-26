def put_call_parity(C,P,S,X,r,T):
    a=C+(1+r)**-T
    b=P+S
    if a==b:
        print("满足期权平价关系")
    else:
        print("不满足期权平价关系，套利策略：买低卖高")