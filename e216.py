from time import time
from script.sieve import *
from script.maths import isprime
from script.tools import miller_rabin as isprime1
def e216(top=50000000):
    t = lambda n:2*n**2-1
    to = round(t(top)**.5)
    print(to)
    global primes
    global p
    p = sieve(to)
    primes = dict.fromkeys(p,1)
    res = 0
    mini=1000
    ttop = t(top)
    for i in range(2,top+1):
        tmp = t(i)
        if i > mini:mini+=1000;print(i/top,end='\r')
        if i<1000:print(i)
        if tmp%2==0:continue
        if isprime1(tmp):res+=1
        #if isprime(tmp,p,ttop):res+=1
    print()
    return res
def isprime2(n):
    if n==2:return True
    if n in (0,1):return False
    if not n&1:return False
    if primes.get(n):return True
    if n<p[-1]:return False
    if any(n%i==0 for i in p):return False
    return True
if __name__=='__main__':
    print(e216(20000))
