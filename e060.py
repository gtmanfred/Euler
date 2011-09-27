#!/usr/bin/env python
'''
from maths import primesd,isprime2
primesdict = primesd(10**4)
p = [x for x in primesdict.keys() if primesdict.get(x) is 1]
'''
#from sys import stderr
from time import time
#from script.maths import isprime2#,primes,primesd,primesd3,isprime
from script.primes import *
#from script.isprime import isprime
#from script.allsieve import soe
t = time()
p = Primes(10**4)
def Euler_60():
    for i in p.pList(10**4):
        print(i)
        p1 = sorted(set(j for j in p.pList(10**4) if j>i and \
            isPrime(str(j)+str(i)) and isPrime(str(i)+str(j))))
        for j in p1:
            p2 = sorted(set(k for k in p1 if k>j and \
                isPrime(str(j)+str(k)) and isPrime(str(k)+str(j))))
            for k in p2:
                p3 = sorted(set(l for l in p2 if l>k and \
                    isPrime(str(k)+str(l)) and isPrime(str(l)+str(k))))
                for l in p3:
                    p4 = sorted(set(m for m in p3 if m>l and \
                        isPrime(str(m)+str(l)) and isPrime(str(l)+str(m))))
                    if len(p4):return [i,j,k,l,p4[0],[i+j+k+l+p4[0]]]
def e60():
    x = primesd3(10**4)
    print('{:>4}'.format('start'))
    for i in x:
        print(str(i))
        p1 = sorted(set(j for j in primesd3(10**4) if j>i and \
            isprime2(str(j)+str(i)) and isprime2(str(i)+str(j))))
        for j in p1:
            p2 = sorted(set(k for k in p1 if k>j and \
                isprime2(str(j)+str(k)) and isprime2(str(k)+str(j))))
            for k in p2:
                p3 = sorted(set(l for l in p2 if l>k and \
                    isprime2(str(k)+str(l)) and isprime2(str(l)+str(k))))
                for l in p3:
                    p4 = sorted(set(m for m in p3 if m>l and \
                        isprime2(str(m)+str(l)) and isprime2(str(l)+str(m))))
                    if len(p4):return [i,j,k,l,p4[0],[i+j+k+l+p4[0]]]
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




if __name__=='__main__':
    t = time()
    #print(e060(),time()-t)
    print(Euler_60(),time()-t)
