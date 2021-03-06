from script.primes import Primes
#from script.sieve import sieve
from script.allsieve import soe
import math
import itertools
from itertools import *
from script.primes import Primes
from time import *
#from script.memorize import *
from script.memo import memo
from operator import mul
from functools import reduce
prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]    # Ensure that this is initialised with at least 1 prime
prime_dict = dict.fromkeys(prime_list, 1)
lastn      = prime_list[-1]
def lcm(n1,n2):
    return (n1*n2)//gcd(n1,n2)
def mullcm(alist):
    tmp = alist[0]
    for i in range(1,len(alist)):
    	 tmp = lcm(tmp,alist[i])
    return tmp

def ncrrec(n,r):
    xn = factrec(n)
    xr = factrec(r)
    nr = factrec(n-r)
    ret = xn/(xr*nr)
    return ret

def ncr(n,r):
    xn = fact(n)
    xr = fact(r)
    nr = fact(n-r)
    ret = xn/(xr*nr)
    return int(ret)

def roots(p):
    """For p prime return all 0 <= x < p satisfying (1+x**3)%p == 0]"""
    if p % 3 != 1: return [p - 1]
    else:
    	 for a in range(2, p):
    	     x = pow(a, (p - 1) // 3, p)
    	     if x != 1:
    	         return[p - x, (-x * x) % p, p - 1]

def nextprime(n):
    """Return the smallest prime larger than or equal to n"""
    n+=1
    if n <= 2:
    	 return 2
    if n % 2 == 0:
    	 n += 1
    while not isprime2(n):
    	 n += 2
    return n

def gcd(a,b=-1):
    if b ==0:return a
    else:return gcd(b,a%b)

def mulgcd(alist):
    tmp = alist[0]
    for i in range(1,len(alist)):
    	 tmp = euclgcd(tmp,alist[i])
    return tmp

def hcf(no1,no2):
    while no1!=no2:
    	 if no1>no2:no1-=no2
    	 elif no2>no1:no2-=no1
    return no1


def pandigs(i = '123456789',d = 9):
    ret = set("".join(x) for x in itertools.permutations(i,d))
    return ret

def ispan(n):
    if type(n)==type(1):
    	 n = str(n)
    #assert len(n)==10,'not enough digits'
    return all(str(i) in n for i in range(1,len(n)+1))

@memo
def factrec(num):
    if num in (0,1):return 1
    else:return num*factrec(num-1)
def fact(num):
    if num==0:return 1
    return reduce(mul,list(range(1,num+1)))
def fact1(num):
    f = num
    if num == 0:
    	 return 1
    if num==1:return 1
    for x in range(1,num):f = f*x
    return f

def primes(n):
    primesdict = primesd(n)
    ret = [x for x in primesdict.keys() if primesdict.get(x) is 1]
    return ret
def primesd3(n):
    x = int(n**.5)
    if n>5*10**7:
    	 t = n//10**7
    	 alist = [0,0,1]
    	 while t>0:
    	     if t==1:alist+=[1,0]*((10**7)//2-1)
    	     else:alist += [1,0]*((10**7)//2)
    	     t-=1
    else:alist = [0,0,1]+[1,0]*((n-1)//2)
    ret = [2]
    nmn = 1000
    for i in range(3,len(alist),2):
    	 #if i>nmn:nmn+=1000;print(i/n,end='\r')
    	 if alist[i]:
    	     ret+=[i]
    	     for y in range(i**2,n,i):alist[y] =0
    return ret

def primesd2(n,s = 0):
    y = 2
    alist = [0 for j in range(s)]
    alist += [1 for i in range(n+1-s)]
    alist[0],alist[1]=0,0
    yield y
    for x in range(4,n,2):alist[x]=0
    for i in range(3,len(alist),2):
    	 if alist[i]:
    	     for y in range(i**2,n,i):alist[y] =0
    	     yield i

def primesd1(n):
    alist = [1 for i in range(n+1)]
    alist[0],alist[1]=0,0
    for x in range(4,n,2):alist[x]=0
    for i in range(3,len(alist),2):
    	 if alist[i]:
    	     for y in range(i**2,n,i):alist[y] =0
    return [x for x in range(len(alist)) if alist[x]]


def primesd(n):
    alist=[i for i in range(3,n+1,2)]
    adict=dict.fromkeys(alist,1)
    adict[2]=1
    for i in range(3,n+1,2):
    	 if adict.get(i):
    	     for y in range(i**2,n,i):adict[y] =0
    print('done')
    return adict


from bisect import bisect_left
# sqrt(1000000000) = 31622
__primes = 0
def plist(n=1000000000):
    global __primes
    __primes = sieve(round(n**.5))
def isprime(n,__primes=0,top = 0):
    if not __primes:__primes = sieve(n)
    # if prime is already in the list, just pick it
    if top==0:top=__primes[-1]
    if n <= top**.5:
    	 i = bisect_left(__primes, n)
    	 return i != len(__primes) and __primes[i] == n
    # Divide by each known prime
    limit = int(n ** .5)
    for p in __primes:
    	 if p > limit: return True
    	 if n % p == 0: return False
    # fall back on trial division if n > 1 billion
    for f in range(nextprime(__primes[-1]), limit, 6): # 31627 is the next prime
    	 if n % f == 0 or n % (f + 4) == 0:
    	     return False
    return True



def primedivs(n=10**7,t = time()):
    alist=[[] for i in range(0,n+1)]
    alist[0],alist[1] = [0],[1]
    for i in range(2,len(alist),2):
    	 x = i//2
    	 alist[i]+=[2]
    	 while x%2==0:
    	     alist[i]+=[2];x=x//2
    print('twos done',time()-t)
    for i in range(3,(n+1)//2+1,2):
    	 if alist[i]==[]:
    	     for y in range(i,len(alist),i):
    	         x = y//i
    	         alist[y]+=[i]
    	         while x%i==0:
    	             alist[y]+=[i];x=x//i
    print('done',time()-t)
    return(alist)

def primetree(num):
    	 if num == 1: return[num]
    	 powers = []
    	 limit = (num/2)+1
    	 i = 2
    	 if isprime2(num): return [num]
    	 while i <= limit:
    	     while num % i == 0:
    	         powers.append(i)
    	         num = num/i
    	     i+=1
    	     if num==1:
    	         break
    	 return powers
def isprime3(num, primes = [2,3,5,7,11,13,17,19]):
    if len(primes)==0:primes = [2,3,5,7,11,13,17,19]
    if num<=primes[-1]:
    	 if num in primes:return True
    	 else:return False
    for i in primes:
    	 if num%i==0:return False
    if num**.5<primes[-1]:return True
    else:
    	 p = soe(int(num**.5)-1)
    	 if p[-1]==primes[-1]:return True
    	 return isprime3(num,p)

def isprime2(num):
    	 if type(num) == str:num = int(num)
    	 if num == 2: return True
    	 if num < 2 or num % 2 == 0: return False
    	 return not any(num % i == 0 for i in range(3,int(math.sqrt(num)), 2))
    	 
def isprime1(n):
    i =2 
    if (n==1):
    	 return False
    if (n==2)or(n==3)or n==5 or n==7 or n==11 or n==13 or n ==17 or n==19:
    	 return True
    
    if (n%2 is 0)or(n%3 is 0)or n%5==9 or n%7==0 or n%11==0 or n%13==0 or n%17==0 or n%19==0:
    	 return False
    while i*i<=n:
    	 if n%i ==0:
    	     return False
    	 i +=1
    return True


def primetree1(num):
    ret = []
    i= 2
    while (isprime1(num) is False):
    	 if (num%i==0):
    	     ret = ret+[i]
    	     num=num//i
    	     i =1
    	 i +=1
    ret = ret + [num]
    return ret

def tree(num):
    ret = [1]
    i= 2
    while (not isprime2(num)):
    	 if (num%i==0):
    	     ret = ret+[i]
    	     ret = ret +[num]
    	     num=num//i
    	     i =1
    	 i +=1
    ret = ret + [num]
    return ret


def ispal(n):
    ns = str(n)
    mid = len(ns)//2
    if ns[:mid]==ns[-mid:][-1::-1]:return True
    else:return False


def ispal2(num):
    num = str(num)
    while len(num)>1:
    	 if num[0] is not num[len(num)-1]:
    	     return False
    	 num = num[1:len(num)-1]
    return True




def _isprime(n):
    ''' Raw check to see if n is prime. Assumes that prime_list is already populated '''
    isprime = n >= 2 and 1 or 0
    for prime in prime_list:	                 # Check for factors with all primes
    	 if prime * prime > n: break             # ... up to sqrt(n)
    	 if not n % prime:
    	     isprime = 0
    	     break
    if isprime: prime_dict[n] = 1	            # Maintain a dictionary for fast lookup
    return isprime

def _refresh(x):
    ''' Refreshes primes upto x '''
    global lastn
    while lastn <= x:	                        # Keep working until we've got up to x
    	     prime_list.append(lastn)            # Maintain a list for sequential access

def prime(x):
    ''' Returns the xth prime '''
    global lastn
    while len(prime_list) <= x:	              # Keep working until we've got the xth prime
    	 lastn = lastn + 1                       # Check the next number
    	 if _isprime(lastn):
    	     prime_list.append(lastn)            # Maintain a list for sequential access
    return prime_list[x]

def isprime_1(x):
    ''' Returns 1 if x is prime, 0 if not. Uses a pre-computed dictionary '''
    _refresh(x)	                              # Compute primes up to x (which is a bit wasteful)
    return prime_dict.get(x, 0)	              # Check if x is in the list

def factors(n):
    ''' Returns a prime factors of n as a list '''
    _refresh(n)
    x, xp, f = 0, prime_list[0], []
    while xp <= n:
    	 if not n % xp:
    	     f.append(xp)
    	     n = n / xp
    	 else:
    	     x = x + 1
    	     xp = prime_list[x]
    return f

def all_factors(n):
    ''' Returns all factors of n, including 1 and n '''
    f = factors(n)
    elts = sorted(set(f))
    numelts = len(elts)
    def gen_inner(i):
    	if i >= numelts:
    	    yield 1
    	    return
    	thiselt = elts[i]
    	thismax = f.count(thiselt)
    	powers = [1]
    	for j in range(thismax):
    	    powers.append(powers[-1] * thiselt)
    	for d in gen_inner(i+1):
    	    for prime_power in powers:
    	        yield prime_power * d
    for d in gen_inner(0):
    	yield d

def num_factors(n):
    ''' Returns the number of factors of n, including 1 and n '''
    div = 1
    x = 0
    while n > 1:
    	 c = 1
    	 while not n % prime(x):
    	     c = c + 1
    	     n = n // prime(x)
    	 x = x + 1
    	 div = div * c
    return div


def sumdigs(var):
    var = str(var)
    ret=0
    for i in range(len(var)):
    	 ret+=int(var[i])
    return ret


def divs(num):
    ret ={1}
    for x in range(2,num//2+2):
    	 if num%x==0:
    	     ret.add(x)
    return ret

def sums(num):
    ret = 0
    if type(num)==type(set()):
    	 while len(num):
    	     ret+=num.pop()
    if type(num)==type(list()):
    	 for x in range(len(num)):
    	     for y in range(len(num[x])):
    	         ret+=num[x][y]
    return ret


letters={'A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','H':'8',\
    	 'I':'9','J':'10','K':'11','L':'12','M':'13','N':'14','O':'15',\
    	 'P':'16','Q':'17','R':'18','S':'19','T':'20','U':'21','V':'22',\
    	 'W':'23','X':'24','Y':'25','Z':'26'}
def findallfactors(num, maxDiv=None):
    factors = []
 
    if maxDiv == None:
    	maxDiv =int(num ** .5) + 1
 
    while True:
    	fst = 2 if len(factors)==0 else factors[-1]
    	r = 2 if fst!=2 else 1
    	for i in range(fst, min(maxDiv, int(num ** .5) + 1),r):
    		# print 'checking', i
    		if num % i==0:
    			factors.append(int(i))
    			num = num // i
    			break
    	else:
    		if num != 1:
    			factors.append(num)
    		break
    return factors

def numfacts(num):
    facts = findallfactors(num)
    fset = set(facts)
    ret = 1
    for n in fset:
    	 ret*=(facts.count(n)+1)
    return ret


def divsieve(n):
    primes = primesd1(n+1)
    primes.insert(1,0)
    alist=[i for i in range(n+1)]
    adict=dict.fromkeys(alist,2)
    adict[0],adict[1]=0,1
    for i in range(2,n+1):
    	 for j in range(i*2,n+1,i):
    	     adict[j] = adict.get(j)+1
    	 '''
    	 for j in range(i*3,i**2+1,i):
    	     if j>n:break
    	     adict[j] = adict.get(j)+adict.get(i)-1
    	 '''
    print('done')
    return adict




if __name__=='__main__':
    t = time()
    a = (primesd3(10**6))
    print(len(a),time()-t)

@memo
def euclgcd(a,b):
    if a==b:return a;
    if (b>a):
    	 return euclgcd(b,a)
    while a>b:
    	 a=a-b
    return euclgcd(b,a)
