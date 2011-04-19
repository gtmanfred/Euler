import maths
def ncr(n,r):
    xn = maths.fact(n)
    xr = maths.fact(r)
    nr = maths.fact(n-r)
    ret = xn/(xr*nr)
    return ret

def Euler_53():
    tot = 0
    for n in range(1,101):
        for r in range(n+1):
            if ncr(n,r)>10**6:
                tot+=1
    return tot

if __name__=='__main__':
    print(Euler_53())
