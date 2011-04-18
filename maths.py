import math
prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]   # Ensure that this is initialised with at least 1 prime
prime_dict = dict.fromkeys(prime_list, 1)
lastn      = prime_list[-1]

def fact(num):
    f = num
    for x in range(1,num):f = f*x
    return f

def primes(n):
    alist=[1 for i in range(n+1)]
    alist[0]=0
    alist[1]=0
    ret =[]
    t = 0
    for i in range(2,len(alist)):
        if alist[i]==1:
            if i>n//2 and t ==0:
                print(i)
                t =1
            for x in range(i**2,len(alist),i):
                alist[x]=0
    for j in range(n+1):
        if alist[j]==1:
            ret = ret+[j]
    return ret

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
        if type(num) != int: return False
        if num == 2: return True
        if num < 2 or num % 2 == 0: return False
        return not any(num % i == 0 for i in range(3,int(math.sqrt(num))+1, 2))

        
def isprime1(n):
    i =2 
    if (n==1):
        return False
    if (n==2)or(n==3):
        return True
    
    if (n%2 is 0) or (n%3 is 0):
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
            n = n / prime(x)
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
        if not num%x:
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
