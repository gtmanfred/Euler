from time import time
from sieve import *
from maths import isprime
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
        #if isprime1(tmp):res+=1
        if isprime(tmp,p,ttop):res+=1
    print()
    return res
def isprime2(n):

def isprime1(n):
    if n==2:return True
    if n in (0,1):return False
    if not n&1:return False
    if primes.get(n):return True
    if n<p[-1]:return False
    for i in p:
        if i>n**.5:return True
        elif n%i==0:return False
    return True
if __name__=='__main__':
    print(e216(10000))
