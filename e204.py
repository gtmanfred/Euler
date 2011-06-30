from functools import reduce
from operator import mul
from sieve import sieve
from maths import fact
from itertools import combinations_with_replacement as comb
from itertools import product
def e204():
    aset = set()
    primes = sieve(100)
    t = 0
    top = fact(len(primes)+30-1)/fact(30)/fact(len(primes)-1)
    mini = 10000
    for j in range(1,31):
        for i in comb(primes,j):
            print(i)
            if t>mini:print(t/top,end='\r');mini+=10000
            aset.add(reduce(mul,i))
            t+=1
    print()
    alist = [i for i in aset if i <= 10**8]
    return len(alist)+1
if __name__=='__main__':
    print(e204())
