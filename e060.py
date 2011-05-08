#!/usr/bin/env python
'''
from maths import primesd,isprime2
primesdict = primesd(10**4)
p = [x for x in primesdict.keys() if primesdict.get(x) is 1]
'''
from primes import Primes
p = Primes(10**4)
def Euler_60():
    for i in p.pList(10**4):
        if i > 13:break
        print(i)
        p1 = sorted(set(j for j in p.pList(10**4) if j>i and \
            p.isPrime(str(j)+str(i)) and p.isPrime(str(i)+str(j))))
        for j in p1:
            p2 = sorted(set(k for k in p1 if k>j and \
                p.isPrime(str(j)+str(k)) and p.isPrime(str(k)+str(j))))
            for k in p2:
                p3 = sorted(set(l for l in p2 if l>k and \
                    p.isPrime(str(k)+str(l)) and p.isPrime(str(l)+str(k))))
                for l in p3:
                    p4 = sorted(set(m for m in p3 if m>l and \
                        p.isPrime(str(m)+str(l)) and p.isPrime(str(l)+str(m))))
                    if len(p4):return [i,j,k,l,p4[0],[i+j+k+l+p4[0]]]


if __name__=='__main__':
 print(Euler_60())
