def e188(a,b,m):
    tmp=1
    while b:
        tmp = pow(a,tmp,10**m)
        b-=1
    return tmp
if __name__=='__main__':
    print(e188(1777,1855,8))
