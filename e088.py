from script.maths import findallfactors
def getMin(k):
    n = k+2
    while True:
        if check(n, k):print(n,k);return n
        n+=1

def check(n,k):
    x = findallfactors(n)
    if len(x)==1:return False
    if len(x)>k:return False
    if sum(x)+k-len(x)>=n:return True
    else:return False


def Euler_88_2(top = 12000):
    aset = set()
    for k in range(2,top+1):
        if k%120==0:print(k//120)
        aset.add(getMin(k))
    ret = 0
    for i in aset:
        ret+=i
    return ret

def Euler_88(N=12000):
    s = [ set([]) for i in range(2*N+1)]
    sol = (N+1)*[0]
    count = 0
    n = 1
    while count < N:
        s[n].add(n-1)
        d = 2
        while d*d <= n:
            if n % d==0:
                for snd in s[n//d]:
                    s[n].add(d+snd-1)
            d = d+1
        for i in s[n]:
            if n-i >= 0 and n-i <= N:
                if sol[n-i] == 0:
                    sol[n-i] = n
                    count = count + 1
                elif sol[n-i] > n:
                    sol[n-i] = n
        n = n+1
    return sum(set(sol[2:]))

if __name__=='__main__':
    print(Euler_88())
