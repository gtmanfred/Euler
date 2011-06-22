from fractions import Fraction as frac
from memorize import memo
from helpers import totient4 as phi
from maths import primetree,primesd3,isprime2,nextprime
from time import time
from math import ceil
from memorize import memo
from maths import roots
def e343(n = 2*10**6):
    a = [1 + k**3 for k in range(n + 1)]
    primes = primesd3(n + 2)
    print()
    for p in primes:
        for s in roots(p):
            for v in range(s, n + 1, p):
                while a[v] > p and a[v] % p == 0:
                    a[v] //= p
    return sum(a) - n - 1

def e343_test(top=2*10**6):
    global primes
    primes = primesd3(top+1)
    print()
    vect = [i**3+1 for i in range(1,top+1)]
    result = 0
    t = time()
    for i in range(len(vect)):
        if i%100==0:print(i)
        vect[i]=max(factors(vect[i]))
        vect[i]=phi(vect[i])
    return sum(vect)
    for k in range(1,top+1):
        i = k**3+1
        j = round(i**(1/3))
        if j%100==0:print(j)
        global primes
        tmp = max(factors(i))#,primes))
        result+=phi(tmp)
    return result
@memo
def factors(n):
    global primes
    p = primes
    if n ==1:return [1]
    if n in p:return [n]
    else:
        for i in range(len(p)):
            if n%p[i]==0:
                result =[p[i]]+factors(n//p[i])#,primes)
                return result
    if isprime2(n):return [n]
    else: 
        primes+=[nextprime(primes[-1])]
        return factors(n)#,primes)

def test():
    with open('f343.txt',encoding='utf-8') as afile:
        f = afile.read()[:-1].split('\n') 
        flist = [i.split(':') for i in f if i!='']
        cache = {}
        for i in flist[:-2]:
            cache[i[0][1:-1]]=int(i[1])
    cache={}
    count = 0
    def ftest(y,x=1): #y=k on the first call
        n = str(frac(x,y)).split('/')
        if len(n)==1:return n
        else:return f(int(n[1])-1,int(n[0])+1)
    @memo
    def f1(k):
        if k==1:return 1
        if cache.get(k):
            return cache.get(k)
        n = frac(1,int(k))
        nx = [str(1),str(k)] 
        alist = []
        while True:
            if len(nx)==1 or nx[1]==1:
                return int(nx[0])
            else:x = nx[0];y = nx[1]
            x=int(x)+1
            y=int(y)-1
            n = frac(x,y)
            nx = str(n).split('/')
            if nx[0]=='1':return f1(nx[1])
    def f(k):
        global cache
        n = frac(1,k)
        nx = [str(1),str(k)] 
        alist = []
        if k==1:return 1
        while True:
            if nx[0]== '1' and len(nx)!=1:alist+=[nx[1]]
            if len(nx)==1 or int(nx[1])==1:
                for i in alist:
                    cache[i]=int(nx[0])
                return int(nx[0])
            else:x = nx[0];y = nx[1]
            x=int(x)+1
            y=int(y)-1
            n = frac(x,y)
            nx = str(n).split('/')
            if nx[0]=='1' and len(nx)!=1 and cache.get(nx[1]):
                global count
                count+=1
                for i in alist:
                    cache[i]=cache.get(nx[1])
                return cache.get(nx[1])
    def e343(tmp=2*10**6):
        global cache
        result = 0
        b = True
        for i in range(1,tmp+1):
            global cache
            print(i)
            result+=f(i**3)
        return result
    try:
        print(e343(100))
        with open('f343.txt',mode='a',encoding='utf-8') as f:
            for i in cache.keys():
                f.write('\n\''+i+'\':'+str(cache.get(i)))
    except:
        with open('f343.txt',mode='a',encoding='utf-8') as f:
            for i in cache.keys():
                f.write('\n\''+i+'\':'+str(cache.get(i)))

if __name__=='__main__':
    t=time()
    print(e343(100))
    print(time()-t)
    t=time()
    print(e343())
    print(time()-t)
