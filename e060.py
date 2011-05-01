'''
from maths import primesd,isprime2
primesdict = primesd(10**4)
p = [x for x in primesdict.keys() if primesdict.get(x) is 1]
'''
from primes import Primes
p = Primes(10**4)
def Euler_60():
    for i in p.pList(10**4):
        p2 = set(j for j in p.pList(10**4) if j>i and
                p.isPrime(str(j)+str(i)) and p.isPrime(str(i)+str(j))
        #for j in p[p.index(i):]:
        for j in p.pList(minval=i):
            a = p.isPrime(int(str(i)+str(j)))
            b = p.isPrime(int(str(j)+str(i)))
            if a and b:
                #for k in p[p.index(j):]:
                for k in p.pList(minval=j):
                    a = p.isPrime(int(str(k)+str(i)))
                    b = p.isPrime(int(str(k)+str(j)))
                    c = p.isPrime(int(str(i)+str(k)))
                    d = p.isPrime(int(str(j)+str(k)))
                    if a and b and c and d:
                        
                        #for l in p[p.index(k):]:
                        '''
                        for l in p.pList(minval=k):
                            a = p.isPrime(int(str(l)+str(i)))
                            b = p.isPrime(int(str(l)+str(j)))
                            c = p.isPrime(int(str(l)+str(k)))
                            d = p.isPrime(int(str(i)+str(l)))
                            e = p.isPrime(int(str(j)+str(l)))
                            f = p.isPrime(int(str(k)+str(l)))
                            if a and b and c and d and e and f:
                                print('i:',i,'j:',j,'k:',k,'l:',l)
                                #for m in p[p.index(l):]:
                                for m in p.pList(minval=l):
                                    a = p.isPrime(int(str(m)+str(i)))
                                    b = p.isPrime(int(str(m)+str(j)))
                                    c = p.isPrime(int(str(m)+str(k)))
                                    d = p.isPrime(int(str(m)+str(l)))
                                    e = p.isPrime(int(str(i)+str(m)))
                                    f = p.isPrime(int(str(j)+str(m)))
                                    g = p.isPrime(int(str(k)+str(m)))
                                    h = p.isPrime(int(str(l)+str(m)))
                                    if a and b and c and d and e and f and g and h:return [[i,j,k,l,m],sum([i,j,k,l,m])]
                        '''
if __name__=='__main__':
 print(Euler_60())
