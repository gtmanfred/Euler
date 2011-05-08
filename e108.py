from divisors import *
from maths import nextprime
from time import time
from facts import numfacts
def e108(sols = 10**3,p = True):
    t = time()
    n = 2
    np = 1
    primes = 2
    test = 100
    while True:
        np = nextprime(np)
        for i in range(primes,primes*np+1,primes):
            if p:count = numfacts(i**2)//2+1
            else:count = numdivs(i**2)//2+1
            if count>test:
                print('n: ',i,'time:',time()-t,'counts:',count,'test: ',test)
                test+=(count//100*100-test+100)
            if count>sols:
                print(time()-t)
                print('n: ',i,'time:',time()-t,'counts:',count);test+=(count//100*100-test+100)
                return i 
        primes *=np

def test(sols = 10**3,np=2,start=2,test = 100):
    t = time()
    n = 2
    z = 2
    primes = 2
    while z<np:primes*=z;z = nextprime(z)
    while True:
        for i in range(start,primes*np+1,primes):
            #count = numfacts(i**2)//2+1
            count = numdivs(i**2)//2+1
            if count>test:
                print('start: ',i,'time:',time()-t,'counts:',count,\
                        'test:',test,'next:',np)
                test+=(count//100*100-test+100)
            if count>sols:
                print(time()-t)
                print('n: ',i,'time:',time()-t,'counts:',count);test+=(count//100*100-test+100)
                return i 
        primes *=np
        np = nextprime(np)
        start = primes


def test1(sols = 10**3):
    t = time()
    test = 100
    n = 1
    while True:
        count = 1
        for i in range(n+1,n*2):
            y = (i*n)/(i-n)
            if y%1==0:count+=1
        if count>test:
            print('n: ',n,'time:',time()-t,'counts:',count);test+=(count//100*100-test+100)
        if count >= sols:print(time()-t);return n
        n+=1
    return 'not finished'

def test2(sols=10**3):
    t = time()
    n = 1
    test = 100
    while True:
        count = (num_factors(n*n)+1)//2
        if count>=sols:print(time()-t);return n
        if count>test:
            print('n: ',n,'time:',time()-t,'counts:',count);test+=(count//100*100-test+100)
        #if count>test:print('n: ',n,'time: ',time()-t,'counts:',count);test+=(count//100*100-test+100)
        #if n%1000==0:print(n)
        #if (num_factors(n*n)+1)//2>=sols:return n
        n+=1
    return n

if __name__=='__main__':
    print(e108(100,True))
    print(e108(100,False))
    print(e108(1000,True))
    print(e108(1000,False))
