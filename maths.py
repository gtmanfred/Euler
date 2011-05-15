from primes import Primes
import math
import itertools
from itertools import *
from primes import Primes
from time import *
prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]   # Ensure that this is initialised with at least 1 prime
prime_dict = dict.fromkeys(prime_list, 1)
lastn      = prime_list[-1]

def memorize(f):
    cache = {}
    def helper(x):
        if x not in cache:            
            cache[x] = f(x)
        return cache[x]
    return helper

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

def gcd(a,b):
    if b ==0:return a
    else:return gcd(b,a%b)

def hcf(no1,no2):
    while no1!=no2:
        if no1>no2:no1-=no2
        elif no2>no1:no2-=no1
    return no1


def pandigs(i = '123456789',d = 9):
    ret = set("".join(x) for x in itertools.permutations(i,d))
    return ret

def ispan(n,ds=9):
    digs = list(str(n))
    if len(digs)<ds:return False
    check = list(str(x) for x in range(1,ds+1))
    if sorted(digs)==check:return True
    else:return False


def fact(num):
    f = num
    if num == 0:
        return 1
    for x in range(1,num):f = f*x
    return f

def primes(n):
    primesdict = primesd(n)
    ret = [x for x in primesdict.keys() if primesdict.get(x) is 1]
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
        if isprime(num): return [num]
        while i <= limit:
            while num % i == 0:
                powers.append(i)
                num = num/i
            i+=1
            if num==1:
                break
        return powers



def isprime2(num):
        if type(num) == str:num = int(num)
        if num == 2: return True
        if num < 2 or num % 2 == 0: return False
        return not any(num % i == 0 for i in range(3,int(math.sqrt(num))+1, 2))

        
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
    while (not isprime(num)):
        if (num%i==0):
            ret = ret+[i]
            ret = ret +[num]
            num=num//i
            i =1
        i +=1
    ret = ret + [num]
    return ret




def ispal(num):
    num = str(num)
    while len(num)>1:
        if num[0] is not num[len(num)-1]:
            return False
        num = num[1:len(num)-1]
    return True




def _isprime(n):
    ''' Raw check to see if n is prime. Assumes that prime_list is already populated '''
    isprime = n >= 2 and 1 or 0
    for prime in prime_list:                    # Check for factors with all primes
        if prime * prime > n: break             # ... up to sqrt(n)
        if not n % prime:
            isprime = 0
            break
    if isprime: prime_dict[n] = 1               # Maintain a dictionary for fast lookup
    return isprime

def _refresh(x):
    ''' Refreshes primes upto x '''
    global lastn
    while lastn <= x:                           # Keep working until we've got up to x
        lastn = lastn + 1                       # Check the next number
        if _isprime(lastn):
            prime_list.append(lastn)            # Maintain a list for sequential access

def prime(x):
    ''' Returns the xth prime '''
    global lastn
    while len(prime_list) <= x:                 # Keep working until we've got the xth prime
        lastn = lastn + 1                       # Check the next number
        if _isprime(lastn):
            prime_list.append(lastn)            # Maintain a list for sequential access
    return prime_list[x]

def isprime(x):
    ''' Returns 1 if x is prime, 0 if not. Uses a pre-computed dictionary '''
    _refresh(x)                                 # Compute primes up to x (which is a bit wasteful)
    return prime_dict.get(x, 0)                 # Check if x is in the list

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
@memorize
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
    print(len(primesd(10**6)),time()-t)
    t = time()
    print(len(primesd1(10**6)),time()-t)
    t = time()
    p = Primes(10**6)
    a = p.pList()
    print(len(a),time()-t)

