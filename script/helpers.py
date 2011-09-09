from collections import defaultdict
from itertools import count
from operator import mul
from functools import reduce
from script.memorize import memo,memo1of2
from script.allsieve import soe as sieve#sieveOfEratosthenes as sieve
#from script.maths import isprime2
from script.primes import isPrime as isprime2
from math import floor
from script.extra import elist
def genindex(alist,f):
    gen = (i for i,x in enumerate(alist) if x == f)
    for i in gen:yield i
def index(alist,f):
    gen = (i for i,x in enumerate(alist) if x == f)
    return list(gen)
def s2l(s):
    return [int(i) for i in s.split(' ')]
def isprime(number):
	if number in (2,3):return True
	if number<=1 or number%2==0:
		return False
	check=3
	maxneeded=number
	while check<maxneeded+1:
		maxneeded=number/check
		if number%check==0:
			return False
		check+=2
	return True

def gcd(a, b):
    while a != 0: a, b = b % a, a
    return b
def lcm(a, b): return a * b / gcd(a, b)
primes_cache, prime_jumps = [], defaultdict(list)
def primes():
    prime = 1
    for i in count():
        if i < len(primes_cache): prime = primes_cache[i]
        else:
            prime += 1
            while prime in prime_jumps:
                for skip in prime_jumps[prime]:
                    prime_jumps[prime + skip] += [skip]
                del prime_jumps[prime]
                prime += 1
            prime_jumps[prime + prime] += [prime]
            primes_cache.append(prime)
        yield prime
def factorize(n):
    for prime in primes():
        if prime > n: return
        exponent = 0
        while n % prime == 0:
            exponent, n = exponent + 1, n / prime
        if exponent != 0:
            yield prime, exponent
#@memo
def totient(n):
    return reduce(mul, ((p-1) * p ** (exp-1) for p, exp in primetree(n)),1)#factorize
def phi(n):
    tmp = lambda p:1-(1/p)
    try:
        return floor(n*reduce(mul,[tmp(i) for i in factors(n)]))
    except:return 1

@memo
def factors(n):
    #allows for easy implimentation without needing to remember
    #[] for memoization on first iteration
    return fs(n,[])
@memo1of2
def fs(n,pfs=[]):
    if isprime2(n):return [n]
    p = sieve(int(n**.5)+1)
    exp = 0
    for i in p:
        if n%i==0:
            while n%i==0:
                n//=i
            pfs+=[i]
            if n==1:return [i]
            return [i]+fs(n,pfs)
def divs(n):
    d = [1]
    for p,e in primetree(n):
        l = len(d)
        d.extend(x*p for i in range(e) for x in d[-l:])
    d.sort()
    return d
def primetree(n):
    tree = fsandexp(n,[])
    p = list(set(tree))
    return [[p[i],tree.count(p[i])] for i in range(len(p))]
#@memo1of2
def fsandexp(n,pfs=[]):
    if n==1:return []
    if isprime2(n):return [n]
    #p = sieve(int(n**.5)+1)
    for i in sieve(int(n**.5)+1):
        if n%i==0:
            n//=i
            pfs+=[i]
            #if n==1:return [i]
            return [i]+fsandexp(n,pfs)
