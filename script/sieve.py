from math import *
def sieve(end):  
    print(end**.5)
    mini = 100
    if end < 2: return []  

    #The array doesn't need to include even numbers  
    lng = ((end//2)-1+end%2)  

    # Create array and assume all numbers in array are prime  
    sieve = [True]*(lng+1)  

    # In the following code, you're going to see some funky  
    # bit shifting and stuff, this is just transforming i and j  
    # so that they represent the proper elements in the array.  
    # The transforming is not optimal, and the number of  
    # operations involved can be reduced.  

    # Only go up to square root of the end  
    for i in range(int(sqrt(end)) >> 1):  
        #sieve out non primes
        if not sieve[i]: continue  

        # Unmark all multiples of i, starting at i**2  
        for j in range( (i*(i + 3) << 1) + 3, lng, (i << 1) + 3):  
            sieve[j] = False  
    # Don't forget 2!  
    primes = [2]  

    # Gather all the primes into a list, leaving out the composite numbers  
    primes.extend([(i << 1) + 3 for i in range(lng) if sieve[i]])  

    print('done')
    return primes

def extendsieve(A, B, pA = []):
    if not pA:pA = sieve(A)
    s = [ True ]* (B-A)
    mini = 1000
    for p in pA:
        # first multiple of p greater than A
        m0 = ((A+p-1)//p)*p
        for m in range( m0, B, p):
            s[m-A] = False
    print('first done')
    limit = int(ceil(sqrt(B)))
    if A%2==0:A+=1
    mini = 50
    for p in range(A,limit+1,2):
        if p<50:print(p,end='\r')
        if p>mini:print(p/limit*2,end='\r');mini+=50
        if s[p-A]:
            for m in range(p*2, B, p):
                s[m-A] = False 
    print('done')
    return [ A+c for (c, isprime) in enumerate(s) if isprime]

import numpy
def prime(upto):
    primes=numpy.arange(3,upto+1,2)
    isprime=numpy.ones((upto-1)/2,dtype=bool)
    for factor in primes[:int(sqrt(upto))]:
        if isprime[(factor-2)/2]: isprime[(factor*3-2)/2::factor]=0
    return numpy.insert(primes[isprime],0,2)
