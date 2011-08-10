from time import time
from functools import reduce
from operator import mul
from maths import gcd,isprime2,isprime3
#from allsieve import primesfrom2to as sieve
from allsieve import sieveOfEratosthenes as sieve
from memorize import *
from helpers import totient as t1
def e214(n=25,t = 4*10**7):
    p = list(sieve(t))
    count = 0
    print('start')
    mini = 1000
    for num in p:
        if num>mini:print(num/p[-1],end='\r');mini+=1000
        if chain(num)==n:count+=num
    return count
@memo
def chain(n):
    if n == 1:return 1
    n = totient(n)
    return 1+chain(n)
@memo
def totient(n):
    return reduce(mul, ((x-1) * x ** (exp-1) for x, exp in primetree(n)),1)#factorize
def primetree(n):
    tree = fsandexp(n,[])
    x = list(set(tree))
    return [[x[i],tree.count(x[i])] for i in range(len(x))]
@memo1of2
def fsandexp(n,pfs=[]):
    if n==1:return []
    if isprime3(n):return [n]
    p = list(sieve(int(n**.5)+1))
    for i in p:
        if n%i==0:
            n//=i
            pfs+=[i]
            #if n==1:return [i]
            return [i]+fsandexp(n,pfs)
if __name__=='__main__':
    '''
    x = 1000
    t = time()
    for i in range(1,x):
        a = totient(i)
    print(time()-t)
    t = time()
    for i in range(1,x):
        a = t1(i)
    print(time()-t)
    '''
    print(e214())
