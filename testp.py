from script.primes import isPrime as ip
#from script.maths import isprime2
from script.isprime import isprime
from time import time
from script.maths import nextprime
from script.prime import is_prime
x = 1000
t = time()
for i in range(1,x):
    a = ip(i)
print(time()-t)
'''
t = time()
for i in range(1,x):
    a = isprime2(i)
print(time()-t)
'''
t = time()
for i in range(1,x):
    a = isprime(i)
print(time()-t)
for i in range(1,x):
    a = is_prime(i)
print(time()-t)
