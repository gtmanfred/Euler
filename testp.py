from primes import isPrime as ip
#from maths import isprime2
from isprime import isprime
from time import time
from maths import nextprime
x = 12
t = time()
for i in range(1,x):
    print(i,end='\r')
    a = ip(nextprime(10**i))
print(time()-t)
'''
t = time()
for i in range(1,x):
    a = isprime2(i)
print(time()-t)
'''
t = time()
for i in range(1,x):
    print(i,end='\r')
    a = isprime(nextprime(10**i))
print(time()-t)
