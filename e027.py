'''
Euler published the remarkable quadratic formula:

    n² + n + 41

    It turns out that the formula will produce 40 primes for the consecutive
    values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41
    is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly
    divisible by 41.

    Using computers, the incredible formula  n²  79n + 1601 was discovered,
    which produces 80 primes for the consecutive values n = 0 to 79. The
    product of the coefficients, 79 and 1601, is 126479.

    Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |4| = 4
    Find the product of the coefficients, a and b, for the quadratic expression
    that produces the maximum number of primes for consecutive values of n,
    starting with n = 0.
'''
#primes = maths.primesd(100000)
from script.allsieve import soe
#from script.isprime import isprime
from script.maths import isprime2 as isprime
primes = dict.fromkeys(soe(10**5),1)
def Euler_27(numa=1000,numb=1000):
    big = 0
    for a in range(-numa,numa):
        print(a/1000,end='\r')
        for b in range(-numb,numb):
            n = 0
            val = n**2+n*a+b
            if isprime(val):
                num = 0
                while isprime(val):
                    num+=1
                    n+=1
                    val = n**2+n*a+b
                if big<n:
                    big = n
                    biga = a
                    bigb = b
    print()
    return [bigb,biga,big]

if __name__=='__main__':
    print(Euler_27())
