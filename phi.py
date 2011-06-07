from maths import *
from time import time
from multiprocessing import Process
'''
if __name__ == '__main__':
    pool = Pool(processes=4)              # start 4 worker processes
    result = pool.apply_async(f, [10])     # evaluate "f(10)" asynchronously
    print result.get(timeout=1)           # prints "100" unless your computer is *very* slow
    print pool.map(f, range(10))
'''
chains = {}
def memo(f):
    cache = {}
    def helper(x):
        if not cache.get(x):cache[x]=f(x)
        return cache.get(x)
    return helper
def memo2(f):
    cache = {}
    def helper(a,b):
        tmp = sorted([a,b])
        p = str(tmp[0])+' '+str(tmp[1])
        if not cache.get(p):cache[p]=f(a,b)
        return cache.get(p)
    return helper
def gcd(a,b):
    if b==0:return a
    else:return gcd(b,a%b)
@memo
def phi(n):
    test = 0
    if isprime2(n):return n-1
    for k in range(1,n):
        if gcd(k,n)==1:test+=1
    return test
@memo
def chain(i):
    if i == 1:return 1
    c = chain(phi(i))+1
    chains[i] = c
    return c
def p():
    global chains
    print(chains)
if __name__=='__main__':
    count = 0
    n = 25
    test = 18000
    lastcount = -1
    primes = primesd3(4*10**7)
    for i in primes[primes.index(18013):]:
        c = chain(i)
        if c==n:print(i,c);count+=1
        if i>test:
            print(i)
            test+=1000
            if lastcount == count:break
            elif count:lastcount = count
    print(count)
