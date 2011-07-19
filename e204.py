from maths import isprime2
from allsieve import sieveOfEratosthenes as sieve
def e204(top=10**8,n=5):
    cou = 0
    while isprime2(n):n+=1
    primes = sieve(int(top**.5))
    for i,x in enumerate(primes):
        if x > n:prime=primes[i:];break
    mini = 10000
    for i in range(1,top):
        if i>mini:print(i/top,end='\r');mini+=10000
        b = True
        if isprime2(i):continue
        for j in primes:
            if j>i**.5:break
            if i%j==0:b = False;break
        if b:cou+=1
    print()
    return cou

if __name__=='__main__':
    print(e204())
