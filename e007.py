from maths import isprime2,primesd3,nextprime
from allsieve import primesfrom2to as sieve
from isprime import isprime

def e007(n=10001):
    x = 3
    i=2
    while i<n:
        if isprime(x):
            i+=1
        x+=2
    return x-2
    '''
    s = 10
    tmp = sieve(s)
    while len(tmp)<n:s*=10;tmp = sieve(s)
    return tmp[n-1]
    '''

def Euler_7(n = 10001):
    p = primesd3(10**6)
    print()
    return p[n-1]
    i =1 
    num = 0;
    while i<n:
        num +=1
        if isprime(num):
            i +=1
    return num 

def isprime(n):
        i =2 
        if (n%2 is 0) or (n%3 is 0):
            return False
        while i*i<=n:
            if n%i ==0:
                return False
            i += 1
        return True

if __name__=='__main__':
    print(e007())
#    print(Euler_7())
