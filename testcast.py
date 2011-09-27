import math
from time import time
def e060():
    x = soe(10**4)
    print('{:>4}'.format('start'))
    for i in x:
        print(str(i))
        p1 = sorted(set(j for j in soe(10**4) if j>i and \
            isprime(str(j)+str(i)) and isprime(str(i)+str(j))))
        for j in p1:
            p2 = sorted(set(k for k in p1 if k>j and \
                isprime(str(j)+str(k)) and isprime(str(k)+str(j))))
            for k in p2:
                p3 = sorted(set(l for l in p2 if l>k and \
                    isprime(str(k)+str(l)) and isprime(str(l)+str(k))))
                for l in p3:
                    p4 = sorted(set(m for m in p3 if m>l and \
                        isprime(str(m)+str(l)) and isprime(str(l)+str(m))))
                    if len(p4):return [i,j,k,l,p4[0],[i+j+k+l+p4[0]]]


def soe(n):
    if n <= 2:
        return []
    sieve = list(range(3, n, 2))
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom-top) // si)
    return [2] + [el for el in sieve if el]

def isprime(n):
    if type(n)==str:
        n = int(n)
    if n in (1,0):
        return False
    elif n<4:
        return True
    elif not n&1:
        return False
    elif n<9:
        return True
    elif not n%3:
        return False
    else:
        r=int(math.sqrt(n))
        f = 5
        while f<=r:
            if not n%f:
                return False
            if not n%(f+2):
                return False
            f = f+6
        return True



if __name__=='__main__':
    t = time()
    print(e060(),time()-t)