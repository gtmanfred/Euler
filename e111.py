#from allsieve import sieveOfEratosthenes as sieve
from itertools import product,combinations
from isprime import isprime
from math2 import digits_to_number
import time
from memorize import *
def e111(n):
    pass
@memo2of2
def M(n,d):
    s = '0123456789'
    maxn = 0
    d = str(d)
    mini = 1000
    for i in product(s,repeat = n): 
        j = ''.join(i)
        if j[0]=='0':continue
        c = j.count(d)
        if d=='0' and c==n-2:return c
        if c>maxn:
            if isprime(int(j)):
                maxn=c
        if maxn==n-1:
            return maxn
    return maxn
    '''
    md = 1
    for i in p:
        if str(i).count(str(d))==n-1:return n-1
        if str(i).count(str(d))>md:md=str(i).count(str(d))
    return md
    '''
def N(n,d):
    count = 0
    nums = []
    m = M(n,d)
    s = '0123456789'
    for j in product(s,repeat = n):
        i = int(''.join(j))
        if len(str(i))==n:
            if not isprime(i):continue
            if str(i).count(str(d))==m:
                count+=1
                nums+=[i]
    return [count,nums]
def S(n,d):
    #[x,y] = N(n,d)
    return sum(y)
if __name__=='__main__':
    x = 10
    count = 0
    d = []
    for i in range(10):
        t = time.time()
        d+=[[i,M(x,i)]]
        print(i,time.time()-t)
    print(d)
        
