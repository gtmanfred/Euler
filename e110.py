from functools import *
from maths import *
 
primes = primes(50)
 
mult = lambda x: reduce(lambda y, z: y * z, x, 1)
 
translate = lambda x: mult(primes[i] ** ((x[i] - 1) // 2) for i in range(len(x)))
 
def generator(limit):
    l = [1] * 14
    while l[13] < limit:
        i = 13
        while i > 0 and (l[i] == l[i-1]):
            l[i] = 1
            i -= 1
        l[i] += 2
        yield l
 
if __name__ == '__main__':
    result = min(translate(l) for l in generator(13) if mult(l) > 8000000)
    print("The result is:", result)
