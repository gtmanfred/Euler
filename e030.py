def Euler_30(num=5,time = 200000):
    ret = sum(x for x in range(2,time) if powers1(x,num)==x)
    return ret

def powers1(n,p):
    s = 0
    while n >0:
        d = n%10
        n = n//10
        s+=d**p
    return s

if __name__=='__main__':
    print(Euler_30())
