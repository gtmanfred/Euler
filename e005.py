import maths
from sieve import sieve
from math import ceil,log
from functools import reduce
from operator import mul
def e005(top=20):
    return reduce(mul,[i**(ceil(log(top)/log(i))-1) for i in sieve(top)])

def Euler_5(top=20):
    val =1
    for i in range(1,top+1):
        if maths.isprime2(i):
            num = i
            while num<=top:
                num = num*i
            val *=(num//i)
    return val
    
if __name__=='__main__':
    print(e005())
    #print(Euler_5())
