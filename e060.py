'''
from maths import primesd,isprime2
primesdict = primesd(10**4)
p = [x for x in primesdict.keys() if primesdict.get(x) is 1]
'''
from primes import Primes
p = Primes(10**4)
def Euler_60():
    for i in p.pList(10**4):
        p1 = set(j for j in p.pList(10**4) if j>i and \
            p.isPrime(str(j)+str(i)) and p.isPrime(str(i)+str(j)))
        for j in p1:
            p2 = set(k for k in p1 if k>j and \
                p.isPrime(str(j)+str(k)) and p.isPrime(str(k)+str(j)))
            for k in p2:
                p3 = set(l for l in p.pList(10**4) if l>k and \
                    p.isPrime(str(k)+str(l)) and p.isPrime(str(l)+str(k)))
                return (p3)



if __name__=='__main__':
 print(Euler_60())
