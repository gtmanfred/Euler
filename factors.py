from sieve import sieve
from maths import isprime2
from memorize import memorize2
@memorize2
def factors(x,i=0):
    if isprime2(x):return [x]
    p = sieve(int(x**.5))
    for j,prime in enumerate(p[i:]):
        tmp = x%prime
        if tmp==0:
            tp = x//prime
            print(tmp,prime)
            return [prime]+factors(tp,j)
    return [x]
